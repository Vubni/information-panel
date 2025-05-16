import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, FSInputFile, InputMediaPhoto
import asyncpg
from datetime import datetime, date
from config import BOT_TOKEN, DB_CONFIG

# Инициализация бота
bot = Bot(token=BOT_TOKEN, base_url="https://school.vubni.com/")
dp = Dispatcher()

# Подключение к БД с автоматическим созданием таблиц
async def get_db_connection():
    conn = await asyncpg.connect(**DB_CONFIG)
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            user_id BIGINT PRIMARY KEY
        )
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) UNIQUE NOT NULL,
            description TEXT NOT NULL,
            date DATE NOT NULL,
            image BYTEA NOT NULL
        )
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS achievements (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) UNIQUE NOT NULL,
            description TEXT NOT NULL,
            date DATE NOT NULL,
            image BYTEA NOT NULL
        )
    ''')
    return conn

# Проверка прав администратора
async def is_admin(user_id: int) -> bool:
    conn = await get_db_connection()
    admin = await conn.fetchrow("SELECT * FROM admins WHERE user_id = $1", user_id)
    await conn.close()
    return admin is not None

# Базовые состояния
class GenericForm(StatesGroup):
    type = State()  # 'event' или 'achievement'
    title = State()
    description = State()
    date = State()
    image = State()

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    help_text = (
        "Добро пожаловать! Доступные команды:\n"
        "/addevent - Добавить новое событие\n"
        "/addachievement - Добавить новое достижение\n"
        "/addadmin <user_id> - Добавить администратора\n"
        "/removeadmin <user_id> - Удалить администратора\n"
        "/help - Показать это сообщение"
    )
    await message.answer(help_text)

# Общая команда для добавления
async def start_add_process(message: Message, state: FSMContext, item_type: str):
    if not await is_admin(message.from_user.id):
        await message.answer("У вас нет прав для этой операции")
        return
        
    await state.update_data(type=item_type)
    await state.set_state(GenericForm.title)
    
    item_name = "события" if item_type == 'event' else "достижения"
    await message.answer(f"Введите название {item_name}:")

# Команда /addevent
@dp.message(Command("addevent"))
async def cmd_add_event(message: Message, state: FSMContext):
    await start_add_process(message, state, 'event')

# Команда /addachievement
@dp.message(Command("addachievement"))
async def cmd_add_achievement(message: Message, state: FSMContext):
    await start_add_process(message, state, 'achievement')

# Добавление администратора
@dp.message(Command("addadmin"))
async def cmd_add_admin(message: Message):
    if not await is_admin(message.from_user.id):
        await message.answer("У вас нет прав для этой операции")
        return

    args = message.text.split()
    if len(args) != 2:
        await message.answer("Использование: /addadmin <user_id>")
        return

    new_admin_id = int(args[1])
    conn = await get_db_connection()
    try:
        await conn.execute("INSERT INTO admins (user_id) VALUES ($1)", new_admin_id)
        await message.answer(f"Администратор {new_admin_id} добавлен")
    except asyncpg.exceptions.UniqueViolationError:
        await message.answer("Этот пользователь уже администратор")
    finally:
        await conn.close()

# Удаление администратора
@dp.message(Command("removeadmin"))
async def cmd_remove_admin(message: Message):
    if not await is_admin(message.from_user.id):
        await message.answer("У вас нет прав для этой операции")
        return

    args = message.text.split()
    if len(args) != 2:
        await message.answer("Использование: /removeadmin <user_id>")
        return

    admin_id = int(args[1])
    conn = await get_db_connection()
    result = await conn.execute("DELETE FROM admins WHERE user_id = $1", admin_id)
    await conn.close()
    
    if result == "DELETE 1":
        await message.answer(f"Администратор {admin_id} удален")
    else:
        await message.answer("Пользователь не был администратором")

# Обработка названия
@dp.message(GenericForm.title)
async def process_title(message: Message, state: FSMContext):
    data = await state.get_data()
    table_name = 'events' if data['type'] == 'event' else 'achievements'
    
    # Проверка на уникальность названия
    conn = await get_db_connection()
    existing = await conn.fetchrow(f"SELECT * FROM {table_name} WHERE title = $1", message.text)
    await conn.close()
    
    if existing:
        await message.answer("Запись с таким названием уже существует. Введите другое название:")
        return
        
    await state.update_data(title=message.text)
    item_name = "события" if data['type'] == 'event' else "достижения"
    await message.answer(f"Введите описание {item_name} (до 200 символов):")
    await state.set_state(GenericForm.description)

# Обработка описания
@dp.message(GenericForm.description)
async def process_description(message: Message, state: FSMContext):
    if len(message.text.strip()) == 0:
        await message.answer("Описание не может быть пустым. Попробуйте еще раз:")
        return
        
    if len(message.text) > 200:
        data = await state.get_data()
        item_type = "события" if data['type'] == 'event' else "достижения"
        await message.answer(f"Описание {item_type} слишком длинное. Попробуйте еще раз:")
        return
    
    await state.update_data(description=message.text)
    data = await state.get_data()
    item_type = "события" if data['type'] == 'event' else "достижения"
    await message.answer(f"Введите дату {item_type} (формат: ГГГГ-ММ-ДД):")
    await state.set_state(GenericForm.date)

# Обработка даты
@dp.message(GenericForm.date)
async def process_date(message: Message, state: FSMContext):
    try:
        input_date = datetime.strptime(message.text.strip(), "%Y-%m-%d").date()
    except ValueError:
        await message.answer("Неверный формат даты. Используйте ГГГГ-ММ-ДД (например, 2025-03-04):")
        return
        
    if input_date < date.today():
        await message.answer("Дата не может быть в прошлом. Введите корректную дату:")
        return
        
    await state.update_data(date=input_date)
    data = await state.get_data()
    item_type = "события" if data['type'] == 'event' else "достижения"
    await message.answer(f"Отправьте изображение для {item_type}:")
    await state.set_state(GenericForm.image)

# Обработка изображения
@dp.message(GenericForm.image, F.photo)
async def process_image(message: Message, state: FSMContext):
    try:
        photo = message.photo[-1]
        image_bytes = (await bot.download(photo)).getvalue()
        data = await state.get_data()
        
        table_name = 'events' if data['type'] == 'event' else 'achievements'
        conn = await get_db_connection()
        
        await conn.execute(f'''
            INSERT INTO {table_name} (title, description, date, image)
            VALUES ($1, $2, $3, $4)
        ''', data['title'], data['description'], data['date'], image_bytes)
        
        success_msg = (
            "Событие успешно добавлено!" 
            if data['type'] == 'event' 
            else "Достижение успешно добавлено!"
        )
        await message.answer(success_msg)
        
    except Exception as e:
        logging.error(e)
        await message.answer("Ошибка при сохранении. Попробуйте снова.")
    finally:
        await conn.close()
        await state.clear()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())