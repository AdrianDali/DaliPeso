# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)
from . import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet(u"background: #F9F6EE;\n"
"border-radius: 5px;\n"
"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.top_bar_frame = QFrame(self.centralwidget)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setGeometry(QRect(10, 10, 781, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_bar_frame.sizePolicy().hasHeightForWidth())
        self.top_bar_frame.setSizePolicy(sizePolicy)
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setBaseSize(QSize(0, 40))
        self.top_bar_frame.setStyleSheet(u"background: #93C059;\n"
"")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.window_title = QLabel(self.top_bar_frame)
        self.window_title.setObjectName(u"window_title")
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(20)
        self.window_title.setFont(font)
        self.window_title.setStyleSheet(u"color: #F9F6EE;")

        self.horizontalLayout_2.addWidget(self.window_title)

        self.window_buttons = QFrame(self.top_bar_frame)
        self.window_buttons.setObjectName(u"window_buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.window_buttons.sizePolicy().hasHeightForWidth())
        self.window_buttons.setSizePolicy(sizePolicy1)
        self.window_buttons.setMinimumSize(QSize(0, 20))
        self.window_buttons.setMaximumSize(QSize(100, 16777215))
        self.window_buttons.setLayoutDirection(Qt.RightToLeft)
        self.window_buttons.setFrameShape(QFrame.NoFrame)
        self.window_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.window_buttons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.close_button = QToolButton(self.window_buttons)
        self.close_button.setObjectName(u"close_button")
        icon = QIcon()
        icon.addFile(u":/iconos/assets/icons/close-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.close_button)

        self.minimize_button = QToolButton(self.window_buttons)
        self.minimize_button.setObjectName(u"minimize_button")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/icons/minimize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.minimize_button)

        self.maximize_button = QToolButton(self.window_buttons)
        self.maximize_button.setObjectName(u"maximize_button")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/icons/maximize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.maximize_button)

        self.restore_button = QToolButton(self.window_buttons)
        self.restore_button.setObjectName(u"restore_button")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/assets/icons/restore-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_button.setIcon(icon3)

        self.horizontalLayout.addWidget(self.restore_button)


        self.horizontalLayout_2.addWidget(self.window_buttons)

        self.main_controls = QWidget(self.centralwidget)
        self.main_controls.setObjectName(u"main_controls")
        self.main_controls.setGeometry(QRect(30, 140, 740, 162))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_controls.sizePolicy().hasHeightForWidth())
        self.main_controls.setSizePolicy(sizePolicy2)
        self.main_controls.setMinimumSize(QSize(740, 0))
        self.main_controls.setMaximumSize(QSize(740, 16777215))
        self.verticalLayout = QVBoxLayout(self.main_controls)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.weghing = QFrame(self.main_controls)
        self.weghing.setObjectName(u"weghing")
        sizePolicy2.setHeightForWidth(self.weghing.sizePolicy().hasHeightForWidth())
        self.weghing.setSizePolicy(sizePolicy2)
        self.weghing.setMinimumSize(QSize(740, 100))
        self.weghing.setMaximumSize(QSize(740, 100))
        self.weghing.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.weghing.setLayoutDirection(Qt.LeftToRight)
        self.weghing.setStyleSheet(u"background: #E9F2DE;\n"
"")
        self.weghing.setFrameShape(QFrame.StyledPanel)
        self.weghing.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.weghing)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(12, -1, -1, -1)
        self.widget = QWidget(self.weghing)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.unit = QLabel(self.widget)
        self.unit.setObjectName(u"unit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.unit.sizePolicy().hasHeightForWidth())
        self.unit.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Orbitron"])
        font1.setPointSize(64)
        font1.setBold(True)
        self.unit.setFont(font1)
        self.unit.setStyleSheet(u"margin: 0px;\n"
"color: #281F10;")
        self.unit.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout_3.addWidget(self.unit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setPointSize(40)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: #281F10;")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_4.addWidget(self.widget)


        self.verticalLayout.addWidget(self.weghing)

        self.widget_2 = QWidget(self.main_controls)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(32)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.new_recipe_button_5 = QPushButton(self.widget_2)
        self.new_recipe_button_5.setObjectName(u"new_recipe_button_5")
        sizePolicy2.setHeightForWidth(self.new_recipe_button_5.sizePolicy().hasHeightForWidth())
        self.new_recipe_button_5.setSizePolicy(sizePolicy2)
        self.new_recipe_button_5.setMinimumSize(QSize(170, 40))
        self.new_recipe_button_5.setMaximumSize(QSize(170, 40))
        self.new_recipe_button_5.setFont(font)
        self.new_recipe_button_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.new_recipe_button_5.setStyleSheet(u"background: rgba(147, 192, 89, 0.4);\n"
"color: #281F10;\n"
"QPushButton{\n"
"	color: white;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/assets/icons/scale_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_recipe_button_5.setIcon(icon4)
        self.new_recipe_button_5.setIconSize(QSize(30, 30))
        self.new_recipe_button_5.setAutoDefault(False)
        self.new_recipe_button_5.setFlat(False)

        self.horizontalLayout_5.addWidget(self.new_recipe_button_5)

        self.new_recipe_button_6 = QPushButton(self.widget_2)
        self.new_recipe_button_6.setObjectName(u"new_recipe_button_6")
        sizePolicy2.setHeightForWidth(self.new_recipe_button_6.sizePolicy().hasHeightForWidth())
        self.new_recipe_button_6.setSizePolicy(sizePolicy2)
        self.new_recipe_button_6.setMinimumSize(QSize(170, 40))
        self.new_recipe_button_6.setMaximumSize(QSize(170, 40))
        self.new_recipe_button_6.setFont(font)
        self.new_recipe_button_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.new_recipe_button_6.setStyleSheet(u"background: rgba(147, 192, 89, 0.4);\n"
"color: #281F10;\n"
"text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/assets/icons/weigth_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_recipe_button_6.setIcon(icon5)
        self.new_recipe_button_6.setIconSize(QSize(30, 30))
        self.new_recipe_button_6.setAutoDefault(False)
        self.new_recipe_button_6.setFlat(False)

        self.horizontalLayout_5.addWidget(self.new_recipe_button_6)

        self.new_recipe_button_7 = QPushButton(self.widget_2)
        self.new_recipe_button_7.setObjectName(u"new_recipe_button_7")
        sizePolicy2.setHeightForWidth(self.new_recipe_button_7.sizePolicy().hasHeightForWidth())
        self.new_recipe_button_7.setSizePolicy(sizePolicy2)
        self.new_recipe_button_7.setMinimumSize(QSize(170, 40))
        self.new_recipe_button_7.setMaximumSize(QSize(170, 40))
        self.new_recipe_button_7.setFont(font)
        self.new_recipe_button_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.new_recipe_button_7.setStyleSheet(u"background: rgba(147, 192, 89, 1);\n"
"color: #281F10;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/assets/icons/add_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_recipe_button_7.setIcon(icon6)
        self.new_recipe_button_7.setIconSize(QSize(30, 30))
        self.new_recipe_button_7.setAutoDefault(False)
        self.new_recipe_button_7.setFlat(False)

        self.horizontalLayout_5.addWidget(self.new_recipe_button_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.registro_table = QTableWidget(self.centralwidget)
        self.registro_table.setObjectName(u"registro_table")
        self.registro_table.setGeometry(QRect(10, 320, 781, 151))
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(588, 60, 201, 51))
        self.widget_3.setStyleSheet(u"background: #E9F2DE;\n"
"border-radius: 5px;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/iconos/assets/icons/user_dark_icon.svg"))

        self.horizontalLayout_6.addWidget(self.label_4)

        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"Rubik"])
        font3.setPointSize(16)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: #281F10;")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamilies([u"Rubik"])
        font4.setPointSize(14)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgba(40, 31, 16, 0.6);")

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_6.addWidget(self.frame)

        self.new_recipe_button_2 = QPushButton(self.centralwidget)
        self.new_recipe_button_2.setObjectName(u"new_recipe_button_2")
        self.new_recipe_button_2.setGeometry(QRect(470, 70, 100, 31))
        font5 = QFont()
        font5.setFamilies([u"Rubik"])
        self.new_recipe_button_2.setFont(font5)
        self.new_recipe_button_2.setStyleSheet(u"background: rgba(147, 192, 89, 1);\n"
"color: #281F10;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.new_recipe_button_5.setDefault(False)
        self.new_recipe_button_6.setDefault(False)
        self.new_recipe_button_7.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"Monitoreo", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.unit.setText(QCoreApplication.translate("MainWindow", u"000.0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.new_recipe_button_5.setText(QCoreApplication.translate("MainWindow", u"Tara", None))
        self.new_recipe_button_6.setText(QCoreApplication.translate("MainWindow", u"Unidades", None))
        self.new_recipe_button_7.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"example@user.com", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"example group", None))
        self.new_recipe_button_2.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

