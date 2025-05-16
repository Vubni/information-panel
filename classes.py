# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project1-2xnALEY.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from core import Tools, VerticalScrollArea, MyWidget
import database as datab

class Ui_Classes(QWidget):
    def __init__(self, tools : Tools, func_window_old, func_window_new):
        super().__init__()
        
        self.tools = tools
        self.func_window_old = func_window_old
        self.func_window_new = func_window_new
        
        if not self.objectName():
            self.setObjectName(u"self")
        self.resize(self.tools.width, self.tools.height)
        self.setStyleSheet(u"color: rgb(255, 255, 255);\n"
f"background-color: {self.tools.color_main};")
        self.centralwidget = MyWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(690, 70))
        self.widget_3.setStyleSheet("background-color: rgba(208, 154, 82, 0);\n"
"color: rgb(255, 255, 210);")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_exit = QPushButton(self.widget_3)
        self.pushButton_exit.setObjectName(u"pushButton_2")
        self.pushButton_exit.setMinimumSize(QSize(60, 60))
        self.pushButton_exit.setMaximumSize(QSize(120, 120))
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


        self.verticalLayout.addWidget(self.widget_3)

        self.frame = VerticalScrollArea(self.centralwidget)
        self.frame.setObjectName(u"frame_2")
        self.frame.setMinimumSize(QSize(680, 1100))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.frame.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(176, 134, 94, 0);")
        self.frame.setWidgetResizable(True)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        # self.widget_2 = QWidget(self.frame)
        # self.widget_2.setObjectName(u"widget_2")
        # self.widget_2.setMinimumSize(QSize(670, 350))
        # self.widget_2.setStyleSheet(f"background-color: {self.tools.color_frame};")
        # self.gridLayout_2 = QGridLayout(self.widget_2)
        # self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.widget_8 = QWidget(self.frame)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(670, 350))
        self.widget_8.setStyleSheet(f"background-color: {self.tools.color_frame};")
        self.gridLayout = QGridLayout(self.widget_8)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)
        

        # self.frame.content_layout.addWidget(self.widget_2)
        self.frame.content_layout.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.frame)
        # self.widget_2.setAttribute(Qt.WA_TransparentForMouseEvents)
        # self.widget_8.setAttribute(Qt.WA_TransparentForMouseEvents)
        # self.widget_2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        self.widget_8.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.pushButton_exit.setText(QCoreApplication.translate("self", u"«", None))
        self.label_4.setText(QCoreApplication.translate("self", u"Выберите класс", None))
        
        self.add_classes_older(datab.get_classes())
        
        self.pushButton_exit.clicked.connect(self.func_window_old)

    # def add_classes_junior(self, button_texts):
    #     for i in reversed(range(self.gridLayout_2.count())): 
    #         widget = self.gridLayout_2.itemAt(i).widget()
    #         if widget is not None:
    #             widget.setParent(None)
    #         else:
    #             self.gridLayout_2.removeItem(self.gridLayout_2.itemAt(i))

    #     # Настройка шрифта и стилей для кнопок
    #     font2 = QFont(self.tools.font_lora)
    #     font2.setWeight(QFont.DemiBold)
    #     font2.setPointSize(52)

    #     button_style = f"background-color: {self.tools.color_widgets};\n" \
    #                 f"color: {self.tools.color_text};"

    #     # Создание кнопок и добавление их в gridLayout_2
    #     row = 0
    #     col = 0
    #     for idx, text in enumerate(button_texts):
    #         button = QPushButton(self.widget_2)
    #         button.setObjectName(f"pushButton_{idx}")
    #         button.setMinimumSize(QSize(320, 150))
    #         button.setFont(font2)
    #         button.setStyleSheet(button_style)
    #         button.setText(text)

    #         # Добавление кнопки в layout
    #         self.gridLayout_2.addWidget(button, row, col, 1, 1)

    #         # Обновление позиции для следующей кнопки
    #         col += 1
    #         if col > 1:  # Максимум 2 кнопки в ряду
    #             col = 0
    #             row += 1

    #     # Добавление вертикальных спейсеров для растяжения
    #     spacer_row = row + (1 if col > 0 else 0)  # Учитываем неполный последний ряд
    #     for col_idx in range(2):  # Добавляем спейсеры в оба столбца
    #         vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    #         self.gridLayout_2.addItem(vertical_spacer, spacer_row, col_idx, 1, 1)

    #     # Автоматическая настройка высоты виджета
    #     total_rows = spacer_row + 1  # Учитываем строки с кнопками и спейсерами
    #     self.widget_2.setMinimumHeight(total_rows * 160 - 160)
    #     self.widget_2.layout().activate()
    #     self.widget_2.adjustSize()
    #     self.frame.content_widget.adjustSize()
    #     self.frame.updateGeometry() 
        
    def add_classes_older(self, button_texts):
        for i in reversed(range(self.gridLayout.count())): 
            widget = self.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
            else:
                self.gridLayout.removeItem(self.gridLayout.itemAt(i))

        # Настройка шрифта и стилей для кнопок
        font2 = QFont(self.tools.font_lora)
        font2.setWeight(QFont.DemiBold)
        font2.setPointSize(52)

        button_style = f"background-color: {self.tools.color_widgets};\n" \
                    f"color: {self.tools.color_text};"

        row = 0
        col = 0
        for text in button_texts:
            button = QPushButton(self.widget_8)
            # Устанавливаем фильтр событий для кнопки
            # button.installEventFilter(self.frame)
            # button.setFocusPolicy(Qt.NoFocus)  # Отключаем фокус
            
            # Настраиваем кнопку
            button.setObjectName(text["class_name"])
            button.setMinimumSize(QSize(320, 150))
            button.setFont(font2)
            button.setStyleSheet(button_style)
            button.setText(text["class_name"])
            button.clicked.connect(self.open_class_info)

            self.gridLayout.addWidget(button, row, col, 1, 1)

            # Обновление позиции для следующей кнопки
            col += 1
            if col > 1:  # Максимум 2 кнопки в ряду
                col = 0
                row += 1

        # Добавление вертикальных спейсеров для растяжения
        spacer_row = row + (1 if col > 0 else 0)  # Учитываем неполный последний ряд
        for col_idx in range(2):  # Добавляем спейсеры в оба столбца
            vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.gridLayout.addItem(vertical_spacer, spacer_row, col_idx, 1, 1)

        # Автоматическая настройка высоты виджета
        total_rows = spacer_row + 1  # Учитываем строки с кнопками и спейсерами
        self.widget_8.setMinimumHeight(total_rows * 160 - 250)
        self.widget_8.layout().activate()
        self.widget_8.adjustSize()
        self.frame.content.adjustSize()
        self.frame.updateGeometry() 
        
    def open_class_info(self):
        sender = self.sender()
        if not sender:
            return
        
        button_name = sender.objectName()
        self.func_window_new(button_name)