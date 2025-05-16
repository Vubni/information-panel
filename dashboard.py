from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QTimer, Signal, QThread,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, 
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel, 
    QMainWindow, QMenuBar, QPushButton, QScrollArea, QGraphicsDropShadowEffect,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
from core import Tools, HorizontalScrollArea, MyWidget
import core
import threading, time
from datetime import datetime
import database as datab

class UpdateWorker(QObject):
    update_trigger = Signal()

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        # Первый запуск сразу при старте
        self.update_trigger.emit()
        
        while self.running:
            # Вычисляем время до начала следующей минуты
            now = datetime.now()
            seconds_until_next_minute = 60 - now.second - now.microsecond / 1e6
            
            # Ждем до начала следующей минуты
            time.sleep(seconds_until_next_minute)
            
            # Проверяем, не остановили ли поток
            if self.running:
                self.update_trigger.emit()

    def stop(self):
        self.running = False
        

class Ui_Dashboard(QWidget):
    def __init__(self, tools : Tools, func_open_classes):
        super().__init__()
        
        self.tools = tools
        self.func_open_classes = func_open_classes
        self.count_update = 9
        
        
        if not self.objectName():
            self.setObjectName(u"self")
        self.resize(self.tools.width, self.tools.height)
        self.setStyleSheet(u"color: rgb(255, 255, 255);\n"
f"background-color: {self.tools.color_main};")
        self.centralwidget = MyWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(680, 60))
        self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont(self.tools.font_playfair)
        font.setPointSize(35)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.label)
        
        

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(680, 270))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setStyleSheet(u"border-radius: 10px;\n"
f"background-color: {self.tools.color_frame};")
        self.verticalLayout_schedule = QVBoxLayout(self.frame_2)
        self.verticalLayout_schedule.setObjectName(u"horizontalLayout")
        
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(650, 30))
        self.label_26.setMaximumSize(QSize(16777215, 40))
        font4 = QFont(self.tools.font_playfair)
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(f"color: {self.tools.color_title};")
        self.label_26.setFrameShadow(QFrame.Shadow.Plain)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_schedule.addWidget(self.label_26)
        
        self.widget_23 = QWidget(self.frame_2)
        self.widget_23.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget_23)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.verticalLayout_schedule.addWidget(self.widget_23)
        
        self.widget = QWidget(self.widget_23)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 225))
        self.widget.setStyleSheet(f"border: 4px solid {self.tools.color_border};\n"
"border-radius: 10px;\n"
f"background-color: {self.tools.color_widgets};\n"
f"color: {self.tools.color_text};")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(235, 100))
        font1 = QFont(self.tools.font_lora)
        font1.setPointSize(40)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet("border: 0px;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(235, 100))
        self.label_3.setStyleSheet("border: 0px;")
        font2 = QFont(self.tools.font_lora)
        font2.setPointSize(24)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_23)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(250, 225))
        self.widget_2.setStyleSheet(
"border-radius: 10px;\n"
f"background-color: {self.tools.color_widgets};\n"
f"color: {self.tools.color_text};")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(235, 100))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(f"color: {self.tools.color_text};")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(235, 100))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.widget_2)

        self.pushButton = QPushButton(self.widget_23)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 225))
        font3 = QFont(self.tools.font_lora)
        font3.setPointSize(110)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(
"text-align: center;\n"
"padding-left: 0;\n"
"padding-right: 0;\n"
"padding-top: -20;\n"
"border-radius: 10px;\n"
f"background-color: {self.tools.color_widgets};\n"
f"color: {self.tools.color_text};")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(680, 307))
        self.frame_4.setStyleSheet(u"border-radius: 10px;\n"
f"background-color: {self.tools.color_frame};")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(650, 30))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        font4 = QFont(self.tools.font_playfair)
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(f"color: {self.tools.color_title};")
        self.label_6.setFrameShadow(QFrame.Shadow.Plain)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_4.addWidget(self.label_6)

        self.scrollArea = HorizontalScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(650, 260))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        

        self.horizontalLayout_3.addStretch()
        self.horizontalLayout_3.addStretch()


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(680, 307))
        self.frame_5.setStyleSheet(u"border-radius: 10px;\n"
f"background-color: {self.tools.color_frame};")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(650, 30))
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(f"color: {self.tools.color_title};")
        self.label_7.setFrameShadow(QFrame.Shadow.Plain)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_5.addWidget(self.label_7)

        self.scrollArea_2 = HorizontalScrollArea(self.frame_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(650, 260))
        self.scrollArea_2.setMouseTracking(False)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 860, 260))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.horizontalLayout_5.addStretch()
        self.horizontalLayout_5.addStretch()

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.scrollArea_3 = QScrollArea(self.centralwidget)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(680, 260))
        self.scrollArea_3.setMaximumSize(QSize(99999, 260))
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollArea_3.setStyleSheet(u"border-radius: 10px;\n"
f"background-color: {self.tools.color_frame};")
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 688, 140))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_15 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_3)
        
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
        
    def add_birthday_greeting(self):
        """Создает виджет с поздравлением"""
        widget = QWidget(self.scrollAreaWidgetContents_4)
        widget.setObjectName(u"greeting_widget")
        widget.setMinimumSize(QSize(500, 130))
        widget.setStyleSheet(f"""
            border-radius: 10px;
            background-color: {self.tools.color_widgets};
            border: 2px solid {self.tools.color_border};
            padding: 10px;
        """)
        
        layout = QVBoxLayout(widget)
        
        font = QFont(self.tools.font_playfair)
        font.setPointSize(25)
        font.setBold(True)
        label = QLabel(widget)
        label.setText(f"""
            <center>
                <b>Поздравляем Никитину Светлану Николаевну с днём рождения💘</b><br>
                <i>- 10Б</i>
            </center>
        """)
        label.setFont(QFont(self.tools.font_lora, 12))
        label.setStyleSheet(f"border: 0px; color: rgb(255, 255, 255); background: transparent;")
        label.setFont(font)
        label.setWordWrap(True)
        
        layout.addWidget(label)
        
        self.horizontalLayout_2.addWidget(widget)
        return widget
        
    def add_widget_events(self, title, description, image, right=True, main=False):
        if right:
            background_color = f"background-color: {self.tools.color_widgets};"
        else:
            background_color = f"background-color: {self.tools.color_widgets_old};"
        
        # Устанавливаем фиксированную ширину виджета для отображения 3.5 виджета в контейнере
        parent_width = self.scrollAreaWidgetContents.width()
        widget_width = parent_width / 3.5  # Рассчитываем ширину для 3.5 виджета
        widget = QWidget(self.scrollAreaWidgetContents)
        widget.setObjectName(u"widget")
        widget.setMinimumSize(QSize(widget_width, 0))  # Устанавливаем рассчитанную ширину
        widget.setMaximumSize(QSize(widget_width, 9999))  # Фиксируем размер
        
        if main:
            widget.setStyleSheet(f"color: {self.tools.color_text};\n"
                                f"border: 4px solid {self.tools.color_border};\n"
                                "border-radius: 10px;\n"
                                + background_color)
        elif not right:
            widget.setStyleSheet(f"color: {self.tools.color_text};\n"
                                "border-radius: 10px;\n"
                                + background_color)
        else:
            widget.setStyleSheet(f"color: {self.tools.color_text};\n"
                                "border-radius: 10px;\n"
                                + background_color)
        
        verticalLayout = QVBoxLayout(widget)
        verticalLayout.setObjectName(u"verticalLayout_8")
        verticalLayout.setContentsMargins(10, 10, 10, 10)  # Добавляем отступы для контента
        
        widget_image = core.ScaledLabel(widget)
        widget_image.setObjectName(u"label_12")
        widget_image.setAlignment(Qt.AlignCenter)
        widget_image.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        widget_image.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                "border: 0px;\n")
        
        # Настройка заголовка и описания
        label_title = QLabel(widget)
        label_title.setWordWrap(True)
        label_title.setFont(QFont(self.tools.font_lora, 12, QFont.Bold))
        label_title.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                "border: 0px;\n")
        
        label_description = QLabel(widget)
        label_description.setWordWrap(True)
        label_description.setFont(QFont(self.tools.font_lora, 10))
        label_description.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                        "border: 0px;\n")
        
        # Расположение элементов
        verticalLayout.addWidget(widget_image, 1)  # Изображение занимает больше места
        verticalLayout.addWidget(label_title, 0, Qt.AlignTop)
        verticalLayout.addWidget(label_description, 0)
        verticalLayout.addStretch(1)
        
        # Загрузка изображения
        pixmap = QPixmap()
        if pixmap.loadFromData(image):
            widget_image.setPixmap(pixmap)
        else:
            widget_image.setText("Нет изображения")
            widget_image.setStyleSheet("background-color: #333;")
        
        label_title.setText(QCoreApplication.translate("self", title, None))
        label_description.setText(QCoreApplication.translate("self", description, None))
        
        # Добавляем виджет в layout с выравниванием по левому краю
        if right:
            self.horizontalLayout_3.insertWidget(self.horizontalLayout_3.count() - 1, widget, alignment=Qt.AlignLeft)
        else:
            self.horizontalLayout_3.insertWidget(1, widget, alignment=Qt.AlignLeft)
        
        # Устанавливаем выравнивание для родительского layout
        self.horizontalLayout_3.setAlignment(Qt.AlignLeft)
        return widget
            
    def center_events_widget(self):
        """Центрирует центральный виджет в видимой области QScrollArea."""
        # Получаем геометрию центрального виджета
        central_widget_width = self.widget_6.width()
        central_widget_pos = self.widget_6.pos().x()
        scroll_bar = self.scrollArea.horizontalScrollBar()
        scroll_bar.setValue(central_widget_pos + central_widget_width // 2 - self.scrollArea.viewport().width() // 2)
        
        
    def add_widget_achievements(self, title, description, image):
        # Расчёт ширины аналогично events
        parent_width = self.scrollAreaWidgetContents_2.width()
        widget_width = parent_width / 3.5  # Сохраняем пропорции 3.5 виджета
        
        # Создание виджета
        widget = QWidget(self.scrollAreaWidgetContents_2)
        widget.setObjectName(u"achievement_widget")
        widget.setMinimumSize(QSize(widget_width, 0))
        widget.setMaximumSize(QSize(widget_width, 9999))
        
        # Настройка стилей с учётом main/right
        gradient = QLinearGradient(0, 0, 0, widget.height())
        gradient.setColorAt(0.0, QColor('#2c3e50'))
        gradient.setColorAt(1.0, QColor('#34495e'))
        
        border_style = "border: 2px solid transparent;"
        widget.setStyleSheet(f"""
            color: {self.tools.color_text};
            border-radius: 10px;
            {border_style}
            background-color: {self.tools.color_widgets};
        """)
        
        # Эффект тени
        widget.setGraphicsEffect(QGraphicsDropShadowEffect(
            blurRadius=10,
            xOffset=3,
            yOffset=3,
            color=QColor(0, 0, 0, 80)
        ))

        # Вертикальный layout с отступами
        verticalLayout = QVBoxLayout(widget)
        verticalLayout.setContentsMargins(10, 10, 10, 10)
        
        # Используем ScaledLabel для изображения (как в events)
        widget_image = core.ScaledLabel(widget)
        widget_image.setAlignment(Qt.AlignCenter)
        widget_image.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        widget_image.setStyleSheet("background: transparent; border: 0px;")
        
        # Заголовок с шрифтом из tools
        label_title = QLabel(widget)
        label_title.setFont(QFont(self.tools.font_lora, 14, QFont.Bold))
        label_title.setWordWrap(True)
        label_title.setStyleSheet(f"background: transparent; border: 0px")
        
        # Описание с шрифтом из tools
        label_description = QLabel(widget)
        label_description.setFont(QFont(self.tools.font_lora, 11))
        label_description.setStyleSheet(f"color: {self.tools.color_description}; border: 0px")
        label_description.setWordWrap(True)
        label_description.setAlignment(Qt.AlignTop)
        
        # Добавление элементов в layout
        verticalLayout.addWidget(widget_image, 1)  # Изображение занимает больше места
        verticalLayout.addWidget(label_title, 0, Qt.AlignTop)
        verticalLayout.addWidget(label_description, 0, Qt.AlignTop)
        verticalLayout.addStretch(1)
        
        # Загрузка изображения
        pixmap = QPixmap()
        if pixmap.loadFromData(image):
            widget_image.setPixmap(pixmap)
        else:
            widget_image.setText("Нет изображения")
            widget_image.setStyleSheet("background: #333; color: white;")
        
        # Установка текста
        label_title.setText(QCoreApplication.translate("self", title, None))
        label_description.setText(QCoreApplication.translate("self", description, None))
        
        # Добавление в layout с учётом позиции
        self.horizontalLayout_5.insertWidget(1, widget, alignment=Qt.AlignLeft)
        
        # Выравнивание родительского layout
        self.horizontalLayout_5.setAlignment(Qt.AlignLeft)
        
        return widget
    
    def center_achievements_widget(self):
        """Центрирует центральный виджет в видимой области QScrollArea."""
        scroll_bar = self.scrollArea_2.horizontalScrollBar()
        scroll_bar.setValue(self.scrollArea.viewport().width())
        
    def add_qr_widget(self, title, filename):
        """Добавляет виджет QR-кода в секцию контактов"""
        widget = QWidget(self.scrollAreaWidgetContents_4)
        widget.setObjectName(u"qr_widget")
        widget.setMinimumSize(QSize(110, 130))
        widget.setStyleSheet(
            "border-radius: 10px;"
            f"background-color: {self.tools.color_widgets};"
        )
        
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Контейнер для изображения
        image_label = QLabel(widget)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Загрузка изображения
        pixmap = QPixmap(f"image/{filename}")  # Папка image в нижнем регистре
        if pixmap.isNull():
            image_label.setText("Нет изображения")
            image_label.setStyleSheet("background: #333; color: white;")
        else:
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
            image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)
        
        # Заголовок
        title_label = QLabel(title, widget)
        title_label.setFont(QFont(self.tools.font_lora, 10))
        title_label.setWordWrap(True)
        title_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        title_label.setStyleSheet(f"color: {self.tools.color_text};")
        
        layout.addWidget(image_label)
        layout.addWidget(title_label)
        
        # Вставляем виджет перед правым спейсером
        self.horizontalLayout_2.insertWidget(
            self.horizontalLayout_2.count() - 1, 
            widget,
            alignment=Qt.AlignLeft
        )
        return widget
        

    def retranslateUi(self):
        self.label.setText(QCoreApplication.translate("self", core.get_current_time(), None))

        current, next_ = datab.get_current_and_next_lesson()
        if current:
            self.label_2.setText(QCoreApplication.translate("self", str(current["lesson_number"]) + " урок", None))
            start = current["start"].strftime('%H:%M')
            stop = current["stop"].strftime('%H:%M')
            self.label_3.setText(QCoreApplication.translate("self", f"{start}-{stop}", None))
        else:
            self.label_2.setText(QCoreApplication.translate("self", "Урока нет", None))
            self.label_3.setText(QCoreApplication.translate("self", f"Уроки закончились.", None))
        if next_:
            self.label_4.setText(QCoreApplication.translate("self", str(next_["lesson_number"]) + " урок", None))
            start = next_["start"].strftime('%H:%M')
            stop = next_["stop"].strftime('%H:%M')
            self.label_5.setText(QCoreApplication.translate("self", f"{start}-{stop}", None))
        else:
            self.label_4.setText(QCoreApplication.translate("self", "Урока нет", None))
            self.label_5.setText(QCoreApplication.translate("self", f"Уроки закончились.", None))
            
        self.pushButton.setText(QCoreApplication.translate("self", u"»", None))
        self.label_26.setText(QCoreApplication.translate("self", "Расписание ", None))
        self.label_6.setText(QCoreApplication.translate("self", u"Мероприятия в лицее", None))
        self.label_7.setText(QCoreApplication.translate("self", u"Наши достижения", None))
        
        self.add_qr_widget("Telegram канал лицея", "channel.jpg")
        self.add_qr_widget("Отзывы и предложения", "feedback.jpg")
        # self.add_birthday_greeting()
        
        self.pushButton.clicked.connect(self.func_open_classes)
        
        self.widget.mousePressEvent = lambda e: self.func_open_classes()
        self.widget_2.mousePressEvent = lambda e: self.func_open_classes()
        # Делаем QLabel прозрачными для кликов
        self.label_2.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.label_3.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.label_4.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.label_5.setAttribute(Qt.WA_TransparentForMouseEvents)
        
        
        self.worker = UpdateWorker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.update_trigger.connect(self.update_time)
        self.thread.start()
        
    def update_time(self):
        self.count_update += 1
        # Обновляем время
        self.label.setText(QCoreApplication.translate("self", core.get_current_time(), None))
        current, next_ = datab.get_current_and_next_lesson()
        if current:
            self.label_2.setText(QCoreApplication.translate("self", str(current["lesson_number"]) + " урок", None))
            start = current["start"].strftime('%H:%M')
            stop = current["stop"].strftime('%H:%M')
            self.label_3.setText(QCoreApplication.translate("self", f"{start}-{stop}", None))
        else:
            self.label_2.setText(QCoreApplication.translate("self", "Урока нет", None))
            self.label_3.setText(QCoreApplication.translate("self", f"Уроки закончились.", None))
        if next_:
            self.label_4.setText(QCoreApplication.translate("self", str(next_["lesson_number"]) + " урок", None))
            start = next_["start"].strftime('%H:%M')
            stop = next_["stop"].strftime('%H:%M')
            self.label_5.setText(QCoreApplication.translate("self", f"{start}-{stop}", None))
        else:
            self.label_4.setText(QCoreApplication.translate("self", "Урока нет", None))
            self.label_5.setText(QCoreApplication.translate("self", f"Уроки закончились.", None))
        if self.count_update == 10:
            self.update_info()
            self.count_update = 0

    def update_info(self):
        now = datetime.now()
        
        # Обновляем мероприятия
        while not data:
            data = datab.get_events()
        # Очищаем старые виджеты
        while self.horizontalLayout_3.count():
            item = self.horizontalLayout_3.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.addStretch()
        self.horizontalLayout_3.addStretch()
        self.scrollAreaWidgetContents.update()
        self.scrollAreaWidgetContents.adjustSize()
        
        first = True
        for item in data:
            if isinstance(item["image"], memoryview):
                item["image"] = item["image"].tobytes() 
            if now.date() > item["date"]:
                self.add_widget_events(item["title"], item["date"].strftime("%d.%m.%Y") + " - " + item["description"], item["image"], False)
                continue
            if first:
                self.widget_6 = self.add_widget_events(item["title"], item["date"].strftime("%d.%m.%Y") + " - " + item["description"], item["image"], main=True)
                first = False
                continue
            self.add_widget_events(item["title"], item["date"].strftime("%d.%m.%Y") + " - " + item["description"], item["image"])
        
        # Обновляем достижения
        while not data:
            data = datab.get_achievements()
        while self.horizontalLayout_5.count():
            item = self.horizontalLayout_5.takeAt(0)
            if item.widget(): item.widget().deleteLater()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.addStretch()
        self.horizontalLayout_5.addStretch()
        self.scrollAreaWidgetContents_2.update()
        self.scrollAreaWidgetContents_2.adjustSize()
            
        
        if data:
            for item in data:
                if isinstance(item["image"], memoryview):
                    item["image"] = item["image"].tobytes() 
                self.add_widget_achievements(item["title"], item["date"].strftime("%d.%m.%Y") + " - " + item["description"], item["image"])
                
        self.scrollAreaWidgetContents.updateGeometry()
        self.scrollAreaWidgetContents_2.updateGeometry()
        QTimer.singleShot(400, self.center_events_widget)
        QTimer.singleShot(400, self.center_achievements_widget)
        


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
    
#     window = Ui_MainWindow()
    
#     sys.exit(app.exec())