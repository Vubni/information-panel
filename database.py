import json
from config import DB_CONFIG
from datetime import datetime
import time
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import OperationalError
from typing import Union, List, Dict

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        """Закрывает текущее соединение (если есть) и создает новое с повторными попытками."""
        if self.connection is not None:
            try:
                self.connection.close()
            except Exception as e:
                print(f"Ошибка при закрытии соединения: {e}")
        while True:
            try:
                self.connection = psycopg2.connect(**DB_CONFIG, cursor_factory=DictCursor)
                self.connection.autocommit = False
                print("Успешное подключение к базе данных")
                return
            except OperationalError as e:
                print(f"Ошибка подключения: {e}. Повторная попытка через 1 сек...")
                time.sleep(1)
            except Exception as e:
                print(f"Критическая ошибка подключения: {e}")
                raise

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            if exc_type is None:
                try:
                    self.connection.commit()
                except Exception as e:
                    print(f"Ошибка при коммите транзакции: {e}")
                    self.connection.rollback()
            else:
                self.connection.rollback()
            try:
                self.connection.close()
            except Exception as e:
                print(f"Ошибка при закрытии соединения: {e}")
            finally:
                self.connection = None

    def execute_with_retry(self, sql: str, params: tuple = (), fetch: str = 'all'):
        """Выполняет SQL-запрос с автоматическим переподключением при ошибках."""
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(sql, params)
                    if sql.strip().lower().startswith('select'):
                        if fetch == 'all':
                            return cursor.fetchall()
                        elif fetch == 'one':
                            return cursor.fetchone()
                    else:
                        return True
            except OperationalError as err:
                print(f"OperationalError: {err}. Попытка переподключения...")
                retry_count += 1
                try:
                    self.connect()
                except Exception as e:
                    print(f"Ошибка переподключения: {e}")
                    time.sleep(1)
            except Exception as e:
                print(f"{e.__class__.__name__}: {e}\nFrom sql: {sql}")
                return False
        return False

    def execute_all(self, sql: str, params: tuple = ()) -> Union[bool, List[Dict]]:
        return self.execute_with_retry(sql, params, fetch='all')

    def execute(self, sql: str, params: tuple = ()) -> Union[bool, Dict]:
        return self.execute_with_retry(sql, params, fetch='one')

    def fetchval(self, sql: str, params: tuple = ()) -> Union[bool, int]:
        try:
            result = self.execute_with_retry(sql, params, fetch='one')
            if result is False:
                return False
            return result[0] if result else None
        except Exception as e:
            print(f"Ошибка в fetchval: {e}")
            return False

    def executemany(self, sql: str, params: List[tuple] = []) -> Union[bool, None]:
        try:
            while True:
                try:
                    with self.connection.cursor() as cursor:
                        if sql.strip().lower().startswith('select'):
                            raise ValueError("Use 'execute' for SELECT queries")
                        cursor.executemany(sql, params)
                        return True
                except OperationalError as err:
                    print(f"OperationalError: {err}. Попытка переподключения...")
                    try:
                        self.connect()
                    except Exception as e:
                        print(f"Ошибка переподключения: {e}")
                        time.sleep(1)
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}\nFrom sql: {sql}")
            return False
        
        

def get_current_and_next_lesson():
    now = datetime.now()
    current_date = now.date()
    current_time = now.time()

    with Database() as db:
        rows = db.execute_all(
            "SELECT * FROM call_schedule WHERE special_day = %s ORDER BY lesson_start ASC",
            (current_date,)
        )
        if not rows:
            # Если нет, проверяем по номеру дня недели
            day_number = now.isoweekday()  # 1 (Понедельник) - 7 (Воскресенье)
            rows = db.execute_all(
                "SELECT * FROM call_schedule WHERE day_number = %s ORDER BY lesson_start ASC",
                (day_number,)
            )
    if not rows:
        return (None, None)

    # Преобразуем строки времени в объекты time
    lessons = []
    for row in rows:
        start_time = row['lesson_start']
        stop_time = row['lesson_stop']
        lessons.append({
            'lesson_number': row['lesson_number'],
            'start': start_time,
            'stop': stop_time
        })

    # Сортируем уроки по времени начала
    lessons.sort(key=lambda x: x['start'])

    current_lesson = None
    next_lesson = None

    # Ищем текущий урок
    for i, lesson in enumerate(lessons):
        if lesson['start'] <= current_time <= lesson['stop']:
            current_lesson = lesson
            if i + 1 < len(lessons):
                next_lesson = lessons[i + 1]
            else:
                next_lesson = None
            break

    if current_lesson is not None:
        return (current_lesson, next_lesson)
    else:
        # Ищем ближайший урок
        for i, lesson in enumerate(lessons):
            if lesson['start'] > current_time:
                next_lesson = lesson
                if i + 1 < len(lessons):
                    next_next_lesson = lessons[i + 1]
                else:
                    next_next_lesson = None
                return (next_lesson, next_next_lesson)
        return (None, None)

def sort_key(item):
    class_name = item["class_name"]
    # Разделяем строку на числовую и буквенную части
    number_part = int(''.join(filter(str.isdigit, class_name)))  # Извлекаем число
    letter_part = ''.join(filter(str.isalpha, class_name))       # Извлекаем букву
    return (number_part, letter_part)

def get_events():
    with Database() as db:
        return db.execute_all("SELECT * FROM events ORDER BY date DESC")

def get_achievements():
    with Database() as db:
        return db.execute_all("SELECT * FROM achievements ORDER BY date DESC")

def get_classes():
    with Database() as db:
        res = db.execute_all("SELECT DISTINCT class_name FROM schedule")
        return sorted(res, key=sort_key, reverse=True)

def get_times_lessons(day_number):
    with Database() as db:
        return db.execute_all("SELECT * FROM call_schedule WHERE day_number=%s ORDER BY lesson_number ASC", (day_number,))
    
def get_lessons(class_name, day_number):
    with Database() as db:
        return db.execute_all("SELECT * FROM schedule WHERE day_number=%s AND class_name=%s ORDER BY lesson_number ASC", (day_number, class_name))