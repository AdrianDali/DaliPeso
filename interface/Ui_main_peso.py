# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_peso.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 637)
        MainWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(MainWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(218, 232, 202);")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.top_bar_frame = QFrame(self.content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #4d705b;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"../../../../../pys6-recipes-organizer/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"../../../../../pys6-recipes-organizer/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"../../../../../pys6-recipes-organizer/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 21, 22))
        icon3 = QIcon()
        icon3.addFile(u"../../../../../pys6-recipes-organizer/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_4.addWidget(self.top_bar_frame)

        self.action_bar_frame = QFrame(self.content_frame)
        self.action_bar_frame.setObjectName(u"action_bar_frame")
        self.action_bar_frame.setMinimumSize(QSize(0, 39))
        self.action_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.action_bar_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.view_button = QPushButton(self.action_bar_frame)
        self.view_button.setObjectName(u"view_button")
        self.view_button.setMinimumSize(QSize(150, 30))
        self.view_button.setFont(font)
        self.view_button.setStyleSheet(u"QPushButton{\n"
"	background-color : #17A2B8;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../pys6-recipes-organizer/assets/icons/view.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_button.setIcon(icon4)
        self.view_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.view_button)

        self.new_recipe_button_2 = QPushButton(self.action_bar_frame)
        self.new_recipe_button_2.setObjectName(u"new_recipe_button_2")
        self.new_recipe_button_2.setMinimumSize(QSize(150, 30))
        self.new_recipe_button_2.setFont(font)
        self.new_recipe_button_2.setStyleSheet(u"QPushButton{\n"
"	background-color : #328f62;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon5 = QIcon()
        icon5.addFile(u"../../../../../pys6-recipes-organizer/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_recipe_button_2.setIcon(icon5)
        self.new_recipe_button_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.new_recipe_button_2)


        self.verticalLayout_4.addWidget(self.action_bar_frame)

        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.administrador_line_edit = QLineEdit(self.frame)
        self.administrador_line_edit.setObjectName(u"administrador_line_edit")
        self.administrador_line_edit.setGeometry(QRect(280, 20, 481, 60))
        self.administrador_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #4d705b;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 20, 61, 51))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.new_recipe_button_5 = QPushButton(self.frame)
        self.new_recipe_button_5.setObjectName(u"new_recipe_button_5")
        self.new_recipe_button_5.setGeometry(QRect(250, 110, 150, 30))
        self.new_recipe_button_5.setMinimumSize(QSize(150, 30))
        self.new_recipe_button_5.setFont(font)
        self.new_recipe_button_5.setStyleSheet(u"QPushButton{\n"
"	background-color : #328f62;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.new_recipe_button_5.setIconSize(QSize(20, 20))
        self.new_recipe_button_6 = QPushButton(self.frame)
        self.new_recipe_button_6.setObjectName(u"new_recipe_button_6")
        self.new_recipe_button_6.setGeometry(QRect(480, 110, 150, 30))
        self.new_recipe_button_6.setMinimumSize(QSize(150, 30))
        self.new_recipe_button_6.setFont(font)
        self.new_recipe_button_6.setStyleSheet(u"QPushButton{\n"
"	background-color : #328f62;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.new_recipe_button_6.setIconSize(QSize(20, 20))
        self.new_recipe_button_7 = QPushButton(self.frame)
        self.new_recipe_button_7.setObjectName(u"new_recipe_button_7")
        self.new_recipe_button_7.setGeometry(QRect(720, 110, 150, 30))
        self.new_recipe_button_7.setMinimumSize(QSize(150, 30))
        self.new_recipe_button_7.setFont(font)
        self.new_recipe_button_7.setStyleSheet(u"QPushButton{\n"
"	background-color : #328f62;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.new_recipe_button_7.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.frame)

        self.registro_table = QTableWidget(self.content_frame)
        self.registro_table.setObjectName(u"registro_table")
        self.registro_table.setContextMenuPolicy(Qt.NoContextMenu)
        self.registro_table.setStyleSheet(u"QTableWidget {\n"
"        gridline-color: #d0d0d0;\n"
"        font: 12pt \"Arial\";\n"
"    }\n"
"\n"
"    QTableWidget::item {\n"
"        color: black;\n"
"        padding: 5px;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #f0f0f0;\n"
"        color: black;\n"
"        padding: 5px;\n"
"        border: 1px solid #d0d0d0;\n"
"    }\n"
"\n"
"    QTableWidget::item:selected {\n"
"        background-color: #b0c4de;\n"
"        color: black;\n"
"    }\n"
"\n"
"    QTableWidget QTableCornerButton::section {\n"
"        background-color: #f0f0f0;\n"
"        border: 1px solid #d0d0d0;\n"
"    }")

        self.verticalLayout_4.addWidget(self.registro_table)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Monitoreo de Peso", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.view_button.setText(QCoreApplication.translate("MainWindow", u"Historial de Registros", None))
        self.new_recipe_button_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.new_recipe_button_5.setText(QCoreApplication.translate("MainWindow", u"Tara", None))
        self.new_recipe_button_6.setText(QCoreApplication.translate("MainWindow", u"Unidades", None))
        self.new_recipe_button_7.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
    # retranslateUi

