from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QPointF, QEvent
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QPushButton, QAbstractButton, QLabel, QSizePolicy
from PySide6 import QtWidgets, QtCore, QtGui
from datetime import datetime
from PySide6.QtGui import QMouseEvent


def load_font(path):
    font_id = QtGui.QFontDatabase.addApplicationFont(path)
    if font_id == -1:
        print("Ошибка загрузки шрифта!")
        return
    font_families = QtGui.QFontDatabase.applicationFontFamilies(font_id)
    if not font_families:
        print("Не удалось получить имя шрифта!")
        return
    return font_families[0]


class Tools():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Стандарт
        # self.color_main = "#F5F5F5"       # Фон окна (светло-серый)
        # self.color_frame = "#E0E0E0"      # Фреймы (серый)
        # self.color_widgets = "#FFFFFF"    # Виджеты (белый)
        # self.color_text = "#2D2D2D"       # Основной текст (темно-серый)
        # self.color_border = "#BDBDBD"     # Границы (средний серый)
        # self.color_title = "#2A5C82"      # Заголовки (синий)
        # self.color_description = "#6D6D6D" # Описания (серый)
        # self.color_widgets_old = "#F0F0F0" # Старые виджеты (светлее)
        
        # # Белый
        # self.color_main = "#F5F5F5"       # Фон окна (светло-серый)
        # self.color_frame = "#E0E0E0"      # Фреймы (серый)
        # self.color_widgets = "#FFFFFF"    # Виджеты (белый)
        # self.color_text = "#2D2D2D"       # Основной текст (темно-серый)
        # self.color_border = "#BDBDBD"     # Границы (средний серый)
        # self.color_title = "#2A5C82"      # Заголовки (синий)
        # self.color_description = "#6D6D6D" # Описания (серый)
        # self.color_widgets_old = "#F0F0F0" # Старые виджеты (светлее)
        
        # Синий
        self.color_main = "#1A1A2E"      # Фон окна (темно-синий)
        self.color_frame = "#16213E"      # Фреймы (темно-синий глубокий)
        self.color_widgets = "#2B3A67"    # Виджеты (сине-серый)
        self.color_text = "#E0E0E0"       # Основной текст (светло-серый)
        self.color_border = "#3A5F99"     # Границы (голубоватый)
        self.color_title = "#BBE1FA"      # Заголовки (голубой)
        self.color_description = "#A0A0A0" # Описания (серый)
        self.color_widgets_old = "#3E4C6D" # Старые виджеты (темнее)
        
        # # Чёрный
        # self.color_main = "#1F1F1F"       # Фон окна (очень темный)
        # self.color_frame = "#2D2D2D"      # Фреймы (темно-серый)
        # self.color_widgets = "#3A3A3A"    # Виджеты (средне-темный)
        # self.color_text = "#FFFFFF"       # Основной текст (белый)
        # self.color_border = "#555555"     # Границы (темно-серый)
        # self.color_title = "#00D1FF"      # Заголовки (электрик-синий)
        # self.color_description = "#A0A0A0" # Описания (светло-серый)
        # self.color_widgets_old = "#444444" # Старые виджеты (темнее)
        
        # # Пушкинские
        # self.color_main = "#F5E6D3"       # Основной фон (пергамент)
        # self.color_frame = "#D4B08C"      # Фреймы (золотой дуб)
        # self.color_widgets = "#E0C9B7"    # Виджеты (старый мрамор)
        # self.color_widgets_old = "#C4B5A6" # Старые виджеты (затемнённый мрамор)
        # self.color_text = "#4A3A2F"       # Основной текст (чернила)
        # self.color_border = "#8B5A2B"     # Границы (антикварная бронза)
        # self.color_title = "#6B2A0F"      # Заголовки (бордовый бархат)
        # self.color_description = "#665544" # Описания (старое дерево)
        # self.color_accent = "#A0522D"     # Акценты (сиена натуральная)
        
        self.font_playfair = load_font("Fonts/PlayfairDisplay.ttf")
        self.font_lora = load_font("Fonts/Lora.ttf")
        


class ScaledLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.original_pixmap = None

    def setPixmap(self, pixmap):
        self.original_pixmap = pixmap
        super().setPixmap(pixmap)

    def resizeEvent(self, event):
        if self.original_pixmap:
            parent = self.parentWidget()
            if parent:
                parent_width = parent.width()
                parent_height = parent.height()
                max_width = parent_width
                max_height = parent_height // 2  # Половина высоты родителя

                # Вычисляем коэффициент масштабирования
                width_ratio = max_width / self.original_pixmap.width()
                height_ratio = max_height / self.original_pixmap.height()
                scale_factor = min(width_ratio, height_ratio)

                # Новые размеры с сохранением пропорций
                scaled_width = int(self.original_pixmap.width() * scale_factor)
                scaled_height = int(self.original_pixmap.height() * scale_factor)

                # Масштабируем изображение
                scaled_pixmap = self.original_pixmap.scaled(
                    scaled_width, scaled_height,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
                super().setPixmap(scaled_pixmap)
        super().resizeEvent(event)
        

class HorizontalScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем видимость горизонтального ползунка
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)    # Отключаем вертикальный ползунок
        
        self._dragging = False
        self._last_mouse_x = 0
        self._velocity = 0  # Скорость движения
        self._friction = 0.95  # Коэффициент трения (замедление)
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._animate_scroll)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = True
            self._last_mouse_x = event.position().x()
            self.setCursor(Qt.ClosedHandCursor)
            self._velocity = 0  # Обнуляем скорость при начале перетаскивания
            self._timer.stop()  # Останавливаем таймер, если он был запущен
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._dragging:
            delta = self._last_mouse_x - event.position().x()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + delta)
            self._last_mouse_x = event.position().x()
            self._velocity = delta  # Сохраняем текущую скорость
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._dragging = False
            self.setCursor(Qt.ArrowCursor)
            if abs(self._velocity) > 1:  # Если скорость достаточно большая, запускаем анимацию
                self._timer.start(16)  # Запускаем таймер (примерно 60 FPS)
        super().mouseReleaseEvent(event)

    def _animate_scroll(self):
        # Уменьшаем скорость с учетом трения
        self._velocity *= self._friction
        if abs(self._velocity) < 0.5:  # Если скорость стала слишком маленькой, останавливаем анимацию
            self._timer.stop()
            return

        # Продолжаем прокрутку с текущей скоростью
        self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + self._velocity)
        
        

class VerticalScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.content = QtWidgets.QWidget()
        self.setWidget(self.content)
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(10)
        
        self.dragging = False
        self.start_pos = QtCore.QPointF()
        self.drag_threshold = 10
        
        self._velocity = 0.0
        self._friction = 0.9
        self.last_mouse_event_time = None
        self.last_mouse_pos = None
        
        self._timer = QTimer(self)
        self._timer.setInterval(16)  # ~60 FPS
        self._timer.timeout.connect(self._animate_scroll)

        self.viewport().installEventFilter(self)

    def eventFilter(self, obj, event: QMouseEvent):
        try:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                if event.button() == QtCore.Qt.LeftButton:
                    self.start_pos = event.globalPosition()
                    self.dragging = False
                    self.last_mouse_event_time = None
                    self.last_mouse_pos = None
                    return obj is self.viewport()

            elif event.type() == QtCore.QEvent.MouseMove:
                if event.buttons() & QtCore.Qt.LeftButton:
                    current_pos = event.globalPosition()
                    
                    if not self.dragging:
                        delta = current_pos - self.start_pos
                        if delta.manhattanLength() > self.drag_threshold:
                            self.dragging = True
                            self.viewport().setCursor(QtCore.Qt.ClosedHandCursor)
                    
                    if self.dragging:
                        current_time = QtCore.QDateTime.currentMSecsSinceEpoch()
                        
                        # Calculate velocity based on movement
                        if self.last_mouse_event_time is not None and self.last_mouse_pos is not None:
                            delta_time = current_time - self.last_mouse_event_time
                            if delta_time > 0:
                                delta_y = (self.last_mouse_pos.y() - current_pos.y())
                                self._velocity = delta_y / delta_time  # pixels/ms
                        
                        self.last_mouse_event_time = current_time
                        self.last_mouse_pos = current_pos
                        
                        if self.start_pos.y() == 0:
                            self.start_pos = event.globalPosition()
                        # Apply immediate drag movement
                        scroll_bar = self.verticalScrollBar()
                        delta_y = int(self.start_pos.y() - current_pos.y())
                        scroll_bar.setValue(scroll_bar.value() + delta_y)
                        self.start_pos = current_pos
                        return True
                    return False

            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                if self.dragging:
                    self.viewport().unsetCursor()
                    self.dragging = False
                    self.start_pos = QtCore.QPointF()
                    
                    # Start animation if sufficient velocity
                    if abs(self._velocity) > 0.1:
                        self._timer.start()
                    return True

        except Exception as e:
            print(f"Error: {str(e)}")
        
        return super().eventFilter(obj, event)
    
    def _animate_scroll(self):
        self._velocity *= self._friction
        scroll_bar = self.verticalScrollBar()
        
        # Calculate movement with frame interval
        delta = self._velocity * self._timer.interval()  # pixels/ms * ms = pixels
        new_value = scroll_bar.value() + delta
        
        # Handle boundaries
        if new_value < scroll_bar.minimum():
            new_value = scroll_bar.minimum()
            self._velocity = 0
        elif new_value > scroll_bar.maximum():
            new_value = scroll_bar.maximum()
            self._velocity = 0
            
        scroll_bar.setValue(int(new_value))
        
        # Stop timer when movement becomes negligible
        if abs(self._velocity) < 0.01:
            self._timer.stop()


        
class MyWidget(QWidget):
    def copy(self):
        # Создаем новый экземпляр того же класса
        copied_widget = self.__class__(parent=self.parent())
        
        # Копируем геометрию
        geometry = self.saveGeometry()
        copied_widget.restoreGeometry(geometry)
        
        # Копируем стили
        copied_widget.setStyleSheet(self.styleSheet())
        
        # Копируем основные свойства
        copied_widget.setEnabled(self.isEnabled())
        copied_widget.setVisible(self.isVisible())
        copied_widget.setWindowTitle(self.windowTitle())
        copied_widget.setWindowOpacity(self.windowOpacity())
        copied_widget.setToolTip(self.toolTip())
        copied_widget.setWhatsThis(self.whatsThis())
        
        # Копируем флаги окна
        copied_widget.setWindowFlags(self.windowFlags())
        
        # Копируем размеры и политики размера
        copied_widget.setFixedSize(self.size())
        copied_widget.setSizePolicy(self.sizePolicy())
        
        # Копируем динамические свойства
        for property_name in self.dynamicPropertyNames():
            value = self.property(property_name.data().decode())
            copied_widget.setProperty(property_name.data().decode(), value)
        
        # Копируем дополнительные атрибуты (если есть)
        if hasattr(self, '__dict__'):
            for key, value in self.__dict__.items():
                if key != '_CopyableWidget__copied':  # Исключаем служебные атрибуты
                    setattr(copied_widget, key, value)
        
        return copied_widget
    
def get_current_and_next_lesson(schedule):
    now = datetime.now()
    current_time = now.time()
    current_day = now.weekday() + 1  # 1-7 (понедельник-воскресенье)

    if current_day not in schedule or not schedule[current_day]:
        return None, None
    
    lessons = sorted(schedule[current_day], key=lambda x: x[0])
    current_lesson = None
    next_lesson = None

    # Поиск текущего урока (если время в промежутке урока)
    for index, lesson in enumerate(lessons):
        start, end = lesson
        if start <= current_time <= end:
            current_lesson = [index] + lesson
            # Следующий урок — следующий в списке после текущего
            next_lesson = [index] + lessons[index + 1] if index + 1 < len(lessons) else None
            break
    else:
        # Если урок не идет, ищем ближайший следующий урок
        for index, lesson in enumerate(lessons):
            if lesson[0] > current_time:
                current_lesson = [index] + lesson
                # Следующий урок — следующий после найденного
                next_lesson = [index] + lessons[index + 1] if index + 1 < len(lessons) else None
                break

    return current_lesson, next_lesson

def is_date_in_current_week(date):
    # Получаем текущую дату
    current_date = datetime.now()
    # Получаем кортеж (год, неделя) для текущей даты и проверяемой даты
    current_week = current_date.isocalendar()[:2]
    date_week = date.isocalendar()[:2]
    # Сравниваем
    return date_week == current_week

def get_current_time():
    # Получаем текущее время
    now = datetime.now()

    # Форматируем дату и время в нужном формате
    formatted_time = now.strftime('%A, %d.%m, %H:%M')

    # Переводим название дня недели на русский язык
    days_translation = {
        'Monday': 'Понедельник',
        'Tuesday': 'Вторник',
        'Wednesday': 'Среда',
        'Thursday': 'Четверг',
        'Friday': 'Пятница',
        'Saturday': 'Суббота',
        'Sunday': 'Воскресенье'
    }

    # Заменяем английское название дня недели на русское
    day_of_week = days_translation[now.strftime('%A')]
    final_formatted_time = formatted_time.replace(now.strftime('%A'), day_of_week)

    return final_formatted_time

def get_day_of_week(date: datetime) -> str:
    # Форматируем дату в нужном формате
    formatted_date = date.strftime('%d.%m')

    # Переводим название дня недели на русский язык
    days_translation = {
        'Monday': 'Понедельник',
        'Tuesday': 'Вторник',
        'Wednesday': 'Среда',
        'Thursday': 'Четверг',
        'Friday': 'Пятница',
        'Saturday': 'Суббота',
        'Sunday': 'Воскресенье'
    }

    # Получаем название дня недели на английском языке
    day_of_week_en = date.strftime('%A')

    # Заменяем английское название дня недели на русское
    day_of_week_ru = days_translation[day_of_week_en]

    # Формируем итоговую строку
    result = f"{day_of_week_ru}, {formatted_date}"

    return result

def sort_json_by_date(json_data, reverse=False):
    """
    Сортирует список словарей по полю 'date'.
    
    :param json_data: Список словарей, где каждый содержит поле 'date' в формате строки.
    :param reverse: Если True, сортирует от самой новой к старой. Если False, от старой к новой.
    :return: Отсортированный список словарей.
    """
    # Определяем функцию для преобразования строки даты в объект datetime
    def get_date(item):
        try:
            # Предполагаем, что дата в формате ISO (например, "2023-10-05")
            return datetime.strptime(item["date"], "%d.%m.%Y")
        except ValueError:
            # Если формат даты другой или пустой, возвращаем минимальную дату
            return datetime.min
    
    # Сортируем данные
    return sorted(json_data, key=get_date, reverse=reverse)