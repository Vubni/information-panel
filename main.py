from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PySide6.QtCore import Qt, QSize, QTimer, QObject, QEvent
from PySide6.QtGui import QFontDatabase, QPainter, QColor
from dashboard import Ui_Dashboard
from classes import Ui_Classes
from lessons import Ui_Lessons
from core import Tools
import datetime


class BlackOverlay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.hide()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 255))

class EventFilter(QObject):
    """Глобальный фильтр событий для отслеживания активности"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def eventFilter(self, obj, event):
        if event.type() in [QEvent.MouseMove, QEvent.KeyPress, QEvent.MouseButtonPress]:
            self.parent.reset_timer()
            if self.parent.black_overlay.isVisible():
                self.parent.showNormalContent()
        return super().eventFilter(obj, event)
    

def load_font(path):
    font_id = QFontDatabase.addApplicationFont(path)
    if font_id == -1:
        print("Ошибка загрузки шрифта!")
        return
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    if not font_families:
        print("Не удалось получить имя шрифта!")
        return
    return font_families[0]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Школьная панель учащегося")
        width, height = 1080, 1920
        self.setGeometry(0, 0, width, height)
        self.setMinimumSize(QSize(width, height))
        
        self.tools = Tools(width, height)
        
        self.setStyleSheet(f"background-color: {self.tools.color_main}; color: {self.tools.color_title}")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.showFullScreen()

        self.show()
        self.dashboard = Ui_Dashboard(self.tools, self.show_window_classes)
        self.classes = Ui_Classes(self.tools, self.show_window_main, self.show_window_lessons)
        self.lessons_widget = None

        self.stacked_widget.addWidget(self.dashboard.centralwidget)
        self.stacked_widget.addWidget(self.classes.centralwidget)

        # Таймер бездействия
        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.setInterval(120000)  # 2 минуты
        self.inactivity_timer.setSingleShot(True)
        self.inactivity_timer.timeout.connect(self.show_window_main)
        
        self.black_overlay = BlackOverlay(self)
        self.black_overlay.setGeometry(0, 0, self.width(), self.height())
        
        self.monitor_timer = QTimer(self)
        self.monitor_timer.timeout.connect(self.check_monitor_state)
        self.monitor_timer.start(60000)  # Проверяем каждую минуту
        self.is_night_mode = False

        # # Запускаем проверку при старте
        # self.check_monitor_state()
        
        # Подключаем обработчик смены виджета
        self.stacked_widget.currentChanged.connect(self.on_current_changed)
        
        # # Устанавливаем глобальный фильтр событий
        # self.event_filter = EventFilter(self)
        # QApplication.instance().installEventFilter(self.event_filter)

        self.show_window_main()

    def check_monitor_state(self):
        now = datetime.datetime.now().time()
        night_time = (now >= datetime.time(19, 0)) or (now < datetime.time(7, 0))

        if night_time and not self.is_night_mode:
            self.show_black_screen()
            self.is_night_mode = True
        elif not night_time and self.is_night_mode:
            self.showNormalContent()
            self.is_night_mode = False

    def show_black_screen(self):
        """Показываем черный экран"""
        self.black_overlay.showFullScreen()
        self.inactivity_timer.stop()

    def showNormalContent(self):
        """Возвращаем нормальное отображение"""
        self.black_overlay.hide()
        self.show_window_main()
        self.inactivity_timer.start()

    def on_current_changed(self):
        """Запускает/останавливает таймер при смене виджета"""
        if self.stacked_widget.currentWidget() != self.dashboard.centralwidget:
            self.inactivity_timer.start()
        else:
            self.inactivity_timer.stop()

    def reset_timer(self):
        """Перезапускает таймер, если текущий виджет не главный"""
        if self.stacked_widget.currentWidget() != self.dashboard.centralwidget:
            self.inactivity_timer.start()

    def show_window_main(self):
        self.stacked_widget.setCurrentWidget(self.dashboard.centralwidget)

    def show_window_classes(self):
        self.stacked_widget.setCurrentWidget(self.classes.centralwidget)

    def show_window_lessons(self, class_name):
        if self.lessons_widget:
            index = self.stacked_widget.indexOf(self.lessons_widget.centralwidget)
            if index != -1:
                self.stacked_widget.removeWidget(self.lessons_widget.centralwidget)
                self.lessons_widget.centralwidget.deleteLater()

        self.lessons_widget = Ui_Lessons(self.tools, class_name, self.show_window_classes)
        self.stacked_widget.addWidget(self.lessons_widget.centralwidget)
        self.stacked_widget.setCurrentWidget(self.lessons_widget.centralwidget)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    import sys
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec())