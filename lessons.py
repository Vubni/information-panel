# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project1-3yiIGeC.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
from core import Tools, MyWidget, get_day_of_week, get_current_time, is_date_in_current_week
from datetime import datetime, timedelta
import database as datab
import random


class Ui_Lessons(QWidget):
    def __init__(self, tools : Tools, class_name, func_window_back):
        super().__init__()
        
        self.class_name = class_name
        self.current_day = datetime.now()
        
        self.tools = tools
        self.func_window_back = func_window_back
        
        if not self.objectName():
            self.setObjectName(u"self")
        self.resize(self.tools.width, self.tools.height)
        self.setStyleSheet(f"color: {self.tools.color_title};\n"
f"background-color: {self.tools.color_main};")
        self.centralwidget = MyWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(690, 70))
        self.widget_3.setStyleSheet("background-color: rgba(208, 154, 82, 0);\n"
f"color: {self.tools.color_title};")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_exit = QPushButton(self.widget_3)
        self.pushButton_exit.setObjectName(u"pushButton_2")
        self.pushButton_exit.setFixedSize(QSize(80, 60))
        font = QFont(self.tools.font_lora)
        font.setPointSize(60)
        font.setBold(True)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet(
"text-align: center;\n"
"padding-left: 0;\n"
"padding-right: 0;\n"
"padding-top: -13;\n"
"border-radius: 10px;\n"
f"background-color: {self.tools.color_widgets};\n"
f"color: {self.tools.color_text};")

        self.horizontalLayout.addWidget(self.pushButton_exit)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(610, 60))
        self.label_4.setMaximumSize(QSize(16777215, 60))
        font1 = QFont(self.tools.font_playfair)
        font1.setPointSize(34)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setFrameShadow(QFrame.Shadow.Plain)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayout.addSpacerItem(QSpacerItem(80, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))


        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(690, 100))
        self.widget_4.setStyleSheet("background-color: rgba(208, 154, 82, 0);\n"
f"color: {self.tools.color_title};")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(420, 60))
        self.label_5.setMaximumSize(QSize(16777215, 60))
        font2 = QFont(self.tools.font_playfair)
        font2.setPointSize(27)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.label_5.setFrameShadow(QFrame.Shadow.Plain)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(680, 1000))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        self.frame_2.setStyleSheet(u"border-radius: 10px;\n"
f"background-color: {self.tools.color_frame};")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_9 = QWidget(self.frame_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(670, 120))
        self.widget_9.setMaximumSize(QSize(16777215, 16777215))
        self.widget_9.setStyleSheet(f"background-color: {self.tools.color_widgets};\n"
f"color: {self.tools.color_text};")
        self.verticalLayout = QVBoxLayout(self.widget_9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_9)
        self.label.setObjectName(u"label")
        font3 = QFont(self.tools.font_lora)
        font3.setPointSize(12)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont(self.tools.font_lora)
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(True)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.verticalSpacer = QSpacerItem(20, 853, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)
        
        self.days_container = QWidget()
        self.days_container.setStyleSheet(f"background-color: {self.tools.color_frame};")
        self.days_container.setFixedHeight(80)  # Высота контейнера

        # Создаем layout для кнопок
        self.days_layout = QHBoxLayout(self.days_container)
        self.days_layout.setContentsMargins(10, 10, 10, 10)  # Отступы
        self.days_layout.setSpacing(10)  # Расстояние между кнопками
        
        self.pushButton_back = QPushButton(self.widget_4)
        self.pushButton_back.setObjectName(u"pushButton_3")
        self.pushButton_back.setFixedHeight(60)
        font_back = QFont(self.tools.font_lora)
        font_back.setPointSize(60)
        self.pushButton_back.setFont(font_back)
        self.pushButton_back.setStyleSheet(
"text-align: center;\n"
"padding-left: 10;\n"
"padding-right: 10;\n"
"padding-top: -17;\n"
"border-radius: 10px;\n"
f"background-color: {self.tools.color_widgets};\n"
f"color: {self.tools.color_text};")
        
        self.days_layout.addWidget(self.pushButton_back)

        # Создаем кнопки
        self.selected_day_button = None  # Для отслеживания выбранной кнопки
        self.days_buttons = []
        days_full = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        
        for day_num in range(6):
            btn = QPushButton(days_full[day_num])
            btn.setFixedSize(147, 60)  # Фиксированный размер для всех кнопок
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.tools.color_widgets};
                    color: {self.tools.color_text};
                    border-radius: 15px;
                    font-size: 22px;
                }}
                QPushButton:hover {{
                    background-color: {self.tools.color_widgets_old};
                }}
            """)
            btn.clicked.connect(lambda _, d=day_num: self.set_day_by_number(d))
            self.days_layout.addWidget(btn)
            self.days_buttons.append(btn)
        
        self.pushButton_next = QPushButton(self.widget_4)
        self.pushButton_next.setObjectName(u"pushButton_4")
        self.pushButton_next.setFixedHeight(60)
        self.pushButton_next.setFont(font_back)
        self.pushButton_next.setStyleSheet(
"text-align: center;\n"
"padding-left: 10;\n"
"padding-right: 10;\n"
"padding-top: -17;\n"
"border-radius: 10px;\n"
f"background-color: {self.tools.color_widgets};\n"
f"color: {self.tools.color_text};")
        
        self.days_layout.addWidget(self.pushButton_next)


        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout_3.addWidget(self.frame_2)
        # Добавляем контейнер с кнопками дней
        self.verticalLayout_3.addWidget(self.days_container)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"self", None))
        self.label_4.setText(QCoreApplication.translate("self", f"Расписание {self.class_name}", None))
        self.label_5.setText(QCoreApplication.translate("self", get_day_of_week(self.current_day), None))
        
        self.pushButton_exit.setText(QCoreApplication.translate("self", u"«", None))
        self.pushButton_exit.clicked.connect(self.func_window_back)
        
        self.pushButton_back.setText(QCoreApplication.translate("self", u"«", None))
        self.pushButton_back.clicked.connect(self.back_day)
        
        self.pushButton_next.setText(QCoreApplication.translate("self", u"»", None))
        self.pushButton_next.clicked.connect(self.next_day)
        
        self.load_lessons()
        
    def set_day_by_number(self, day_num):
        self.update_date_buttons(day_num)

        # Остальная логика обработки даты
        self.current_day += timedelta(days=day_num+1)
        self.load_lessons()
        
    def update_days_buttons(self):
        current_weekday = self.current_day.weekday()
        for i, btn in enumerate(self.days_buttons):
            if i == current_weekday:
                btn.setStyleSheet(
        f"background-color: {self.tools.color_frame};"
        f"color: {self.tools.color_text};"
        "border-radius: 15px;"
        "padding: 8px;"
    )
                
    def update_date_buttons(self, number_day):            
        if self.selected_day_button:
            # Восстанавливаем стиль предыдущей выбранной кнопки
            self.selected_day_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {self.tools.color_widgets};
                    color: {self.tools.color_text};
                    border-radius: 15px;
                    font-size: 22px;
                }}
                QPushButton:hover {{
                    background-color: {self.tools.color_widgets_old};
                }}
            """)
            self.selected_day_button.setEnabled(True)
        
        if number_day == 6:
            return
        selected_btn = self.days_buttons[number_day]
        selected_btn.setEnabled(False)
        selected_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.tools.color_widgets_old};
                color: {self.tools.color_text};
                border-radius: 15px;
                font-size: 22px;
            }}
        """)
        self.selected_day_button = selected_btn
        
    def back_day(self):
        self.current_day -= timedelta(days=1)
        self.load_lessons()
        
    def next_day(self):
        self.current_day += timedelta(days=1)
        self.load_lessons()
        
    def load_lessons(self):
        if self.current_day.date() == datetime.now().date():
            self.label_5.setText(QCoreApplication.translate("self", get_current_time(), None))
        else:
            self.label_5.setText(QCoreApplication.translate("self", get_day_of_week(self.current_day), None))
        
        if is_date_in_current_week(self.current_day) or self.current_day.weekday() == 6:
            self.update_date_buttons(self.current_day.weekday())
        
        # Очищаем предыдущие уроки
        while self.verticalLayout_2.count():
            item = self.verticalLayout_2.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                self.verticalLayout_2.removeItem(item)
        
        # Проверяем текущий день (воскресенье не обрабатываем)
        weekday = self.current_day.weekday() + 1
        if weekday == 7:  # Воскресенье
            quotes = [
                "Образование — это то, что остаётся, когда забываешь всё, чему учили. (Альберт Эйнштейн)",
                "Учиться можно только весело... Чтобы переваривать знания, надо поглощать их с аппетитом. (Анатоль Франс)",
                "Знание — сила. (Фрэнсис Бэкон)",
                "Не для школы, а для жизни мы учимся. (Сенека)",
                "Успех — это умение двигаться от неудачи к неудаче, не теряя энтузиазма. (Уинстон Черчилль)",
                "Образование — самое мощное оружие, которым можно изменить мир. (Нельсон Мандела)",
                "Ученье без размышления бесполезно, но и размышление без ученья опасно. (Конфуций)",
                "Книги — это корабли мысли, странствующие по волнам времени. (Фрэнсис Бэкон)",
                "Тот, кто не стремится к образованию, уже мёртв. (Пророк Мухаммед)",
                "Лучше учиться и не знать, чем не учиться и думать, что знаешь. (Китайская пословица)",
                "Упорство и труд — вот залог успеха в учёбе.",
                "Каждая книга открывает новые горизонты.",
                "Учиться никогда не поздно. (Пословица)",
                "Знания приобретаются трудом, а не мечтами.",
                "Учеба — это путь к самосовершенствованию.",
                "Великие умы обсуждают идеи, средние — события, малые — людей. (Элеонора Рузвельт)",
                "Не бойся расти медленно, бойся стоять на месте. (Китайская пословица)",
                "Учиться, учиться и ещё раз учиться! (В.И. Ленин)",
                "Сначала накопляй знания; они — основа всякого совершенства. (Иммануил Кант)",
                "Успех — это 1% таланта и 99% труда. (Томас Эдисон)",
                "Учение — это не подготовка к жизни, учение — сама жизнь. (Джон Дьюи)",
                "Тот, кто не хочет учиться, не достоин человеческого общества. (Платон)",
                "Знание только тогда знание, когда оно приобретено усилиями своей мысли. (Лев Толстой)",
                "Стремись не к тому, чтобы добиться успеха, а к тому, чтобы твоя жизнь имела смысл. (Альберт Эйнштейн)",
                "Учиться можно только с настроением. (Александр Герцен)",
                "Лучший способ изучить что-либо — это открыть самому. (Дьёрдь Пойа)",
                "Образование не даёт ростков в душе, если оно не проникает до значительной глубины. (Протагор)",
                "Ученье — путь к умению. (Русская пословица)"
            ]
            self.show_empty_message(random.choice(quotes))  # Или random.choice(quotes)
            return
        
        data = datab.get_lessons(self.class_name, weekday)
        times = datab.get_times_lessons(weekday)
        
        if not data:
            # Создаем сообщение об отсутствии уроков
            self.show_empty_message("На этот день уроков нет")
            return
        
        temp = None
        current_lesson = None
        now = datetime.now()
        current_time = now.time()
        for i in range(len(times)):
            if i+1 > data[-1]["lesson_number"]:
                break
            if temp is None:
                if data[0]["lesson_number"] != i+1:
                    continue
                temp = i
            lesson_name, lesson_rooms = data[i-temp]["lesson_name"], data[i-temp]["offices"]
            start_time = times[i]["lesson_start"].strftime("%H:%M")
            end_time = times[i]["lesson_stop"].strftime("%H:%M")
            
            start_datetime = datetime.combine(now.date(), times[i]["lesson_start"])
            time_diff = start_datetime - now

            # Создаем виджет урока
            widget_lesson = QWidget()
            widget_lesson.setMinimumSize(QSize(670, 150))
            widget_lesson.setStyleSheet(
                f"background-color: {self.tools.color_widgets};"
                f"color: {self.tools.color_text};"
            )
            if now.date() == self.current_day.date():
                if times[i]["lesson_start"] <= current_time <= times[i]["lesson_stop"] or (not current_lesson and time_diff <= timedelta(minutes=40) and time_diff > timedelta(0)):
                    current_lesson = True
                    widget_lesson.setStyleSheet(
                        f"background-color: {self.tools.color_widgets};"
                        f"color: {self.tools.color_text};"
                        f"border: 4px solid {self.tools.color_border};\n"
                    )
            layout = QVBoxLayout(widget_lesson)
            layout.setSpacing(8)
            
            # Номер урока
            lbl_number = QLabel(f"{i+1} урок")
            lbl_number.setFont(QFont(self.tools.font_lora, 14, QFont.Bold))
            lbl_number.setAlignment(Qt.AlignCenter)
            lbl_number.setStyleSheet("border: 0px")
            layout.addWidget(lbl_number)
            
            # Название урока
            lbl_name = QLabel(lesson_name)
            lbl_name.setFont(QFont(self.tools.font_lora, 16, QFont.Bold))
            lbl_name.setAlignment(Qt.AlignCenter)
            lbl_name.setStyleSheet("border: 0px")
            layout.addWidget(lbl_name)
            
            # Время
            lbl_time = QLabel(f"{start_time} - {end_time}")
            lbl_time.setFont(QFont(self.tools.font_lora, 14, italic=True))
            lbl_time.setAlignment(Qt.AlignCenter)
            lbl_time.setStyleSheet("border: 0px")
            layout.addWidget(lbl_time)
            
            # Кабинеты
            lbl_rooms = QLabel(f"Кабинеты: {lesson_rooms}")
            lbl_rooms.setFont(QFont(self.tools.font_lora, 14, italic=True))
            lbl_rooms.setAlignment(Qt.AlignCenter)
            lbl_rooms.setStyleSheet("border: 0px")
            layout.addWidget(lbl_rooms)
            
            self.verticalLayout_2.addWidget(widget_lesson)
            
        
        # Добавляем спейсер только если есть уроки
        self.verticalLayout_2.addItem(
            QSpacerItem(20, 853, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

    def show_empty_message(self, message_text):
        message_widget = QWidget()
        message_widget.setMinimumSize(QSize(670, 250))  # Увеличенный размер
        message_widget.setStyleSheet(
            f"background-color: {self.tools.color_widgets};"
            f"color: {self.tools.color_text};"
            "border-radius: 10px;"
            "padding: 20px;"
        )
        
        layout = QVBoxLayout(message_widget)
        layout.setContentsMargins(20, 20, 20, 20)  # Отступы внутри виджета
        
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        message_label = QLabel(message_text)
        message_label.setFont(QFont(self.tools.font_playfair, 28, QFont.Bold))  # Больший шрифт
        message_label.setAlignment(Qt.AlignCenter)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("margin: 20px;")  # Дополнительные отступы
        
        layout.addWidget(message_label)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.verticalLayout_2.addWidget(message_widget)
