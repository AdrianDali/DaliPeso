# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
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
        self.background_frame = QFrame(self.centralwidget)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setGeometry(QRect(0, 0, 800, 480))
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.top_bar_frame = QFrame(self.background_frame)
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
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconos/assets/icons/close-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.close_button)

        self.minimize_button = QToolButton(self.window_buttons)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/icons/minimize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.minimize_button)

        self.maximize_button = QToolButton(self.window_buttons)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/icons/maximize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.maximize_button)

        self.restore_button = QToolButton(self.window_buttons)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconos/assets/icons/restore-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_button.setIcon(icon3)

        self.horizontalLayout.addWidget(self.restore_button)


        self.horizontalLayout_2.addWidget(self.window_buttons)

        self.main_controls = QWidget(self.background_frame)
        self.main_controls.setObjectName(u"main_controls")
        self.main_controls.setGeometry(QRect(30, 130, 740, 162))
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

        self.feature_buttons = QWidget(self.main_controls)
        self.feature_buttons.setObjectName(u"feature_buttons")
        self.horizontalLayout_5 = QHBoxLayout(self.feature_buttons)
        self.horizontalLayout_5.setSpacing(32)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.tare_button = QPushButton(self.feature_buttons)
        self.tare_button.setObjectName(u"tare_button")
        sizePolicy2.setHeightForWidth(self.tare_button.sizePolicy().hasHeightForWidth())
        self.tare_button.setSizePolicy(sizePolicy2)
        self.tare_button.setMinimumSize(QSize(170, 40))
        self.tare_button.setMaximumSize(QSize(170, 40))
        self.tare_button.setFont(font)
        self.tare_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tare_button.setStyleSheet(u"background: rgba(147, 192, 89, 0.4);\n"
"color: #281F10;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/assets/icons/scale_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tare_button.setIcon(icon4)
        self.tare_button.setIconSize(QSize(30, 30))
        self.tare_button.setAutoDefault(False)
        self.tare_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.tare_button)

        self.units_button = QPushButton(self.feature_buttons)
        self.units_button.setObjectName(u"units_button")
        sizePolicy2.setHeightForWidth(self.units_button.sizePolicy().hasHeightForWidth())
        self.units_button.setSizePolicy(sizePolicy2)
        self.units_button.setMinimumSize(QSize(170, 40))
        self.units_button.setMaximumSize(QSize(170, 40))
        self.units_button.setFont(font)
        self.units_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.units_button.setStyleSheet(u"background: rgba(147, 192, 89, 0.4);\n"
"color: #281F10;")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/assets/icons/weigth_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.units_button.setIcon(icon5)
        self.units_button.setIconSize(QSize(30, 30))
        self.units_button.setAutoDefault(False)
        self.units_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.units_button)

        self.new_record_button = QPushButton(self.feature_buttons)
        self.new_record_button.setObjectName(u"new_record_button")
        sizePolicy2.setHeightForWidth(self.new_record_button.sizePolicy().hasHeightForWidth())
        self.new_record_button.setSizePolicy(sizePolicy2)
        self.new_record_button.setMinimumSize(QSize(170, 40))
        self.new_record_button.setMaximumSize(QSize(170, 40))
        self.new_record_button.setFont(font)
        self.new_record_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.new_record_button.setStyleSheet(u"background: rgba(147, 192, 89, 1);\n"
"color: #281F10;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/assets/icons/add_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.new_record_button.setIcon(icon6)
        self.new_record_button.setIconSize(QSize(30, 30))
        self.new_record_button.setAutoDefault(False)
        self.new_record_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.new_record_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.feature_buttons)

        self.registro_table = QTableWidget(self.background_frame)
        self.registro_table.setObjectName(u"registro_table")
        self.registro_table.setGeometry(QRect(0, 310, 800, 171))
        self.session_frame = QFrame(self.background_frame)
        self.session_frame.setObjectName(u"session_frame")
        self.session_frame.setGeometry(QRect(370, 60, 411, 51))
        self.session_frame.setFrameShape(QFrame.StyledPanel)
        self.session_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.session_frame)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.login_button = QPushButton(self.session_frame)
        self.login_button.setObjectName(u"login_button")
        sizePolicy2.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy2)
        self.login_button.setMinimumSize(QSize(130, 30))
        font3 = QFont()
        font3.setFamilies([u"Rubik"])
        font3.setPointSize(16)
        self.login_button.setFont(font3)
        self.login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_button.setStyleSheet(u"background: rgba(147, 192, 89, 1);\n"
"color: #281F10;")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/assets/icons/user_outlined_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.login_button.setIcon(icon7)
        self.login_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.login_button)

        self.user_info_frame = QFrame(self.session_frame)
        self.user_info_frame.setObjectName(u"user_info_frame")
        self.user_info_frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.user_info_frame.setStyleSheet(u"background: #E9F2DE;\n"
"border-radius: 5px;")
        self.horizontalLayout_6 = QHBoxLayout(self.user_info_frame)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.user_icon = QLabel(self.user_info_frame)
        self.user_icon.setObjectName(u"user_icon")
        self.user_icon.setPixmap(QPixmap(u":/iconos/assets/icons/user_dark_icon.svg"))

        self.horizontalLayout_6.addWidget(self.user_icon)

        self.user_info = QFrame(self.user_info_frame)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setFrameShape(QFrame.StyledPanel)
        self.user_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.user_info)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user_email_label = QLabel(self.user_info)
        self.user_email_label.setObjectName(u"user_email_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.user_email_label.sizePolicy().hasHeightForWidth())
        self.user_email_label.setSizePolicy(sizePolicy4)
        self.user_email_label.setFont(font3)
        self.user_email_label.setStyleSheet(u"color: #281F10;")
        self.user_email_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.user_email_label)

        self.user_gruop_label = QLabel(self.user_info)
        self.user_gruop_label.setObjectName(u"user_gruop_label")
        sizePolicy4.setHeightForWidth(self.user_gruop_label.sizePolicy().hasHeightForWidth())
        self.user_gruop_label.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Rubik"])
        font4.setPointSize(14)
        self.user_gruop_label.setFont(font4)
        self.user_gruop_label.setStyleSheet(u"color: rgba(40, 31, 16, 0.6);")
        self.user_gruop_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.user_gruop_label)


        self.horizontalLayout_6.addWidget(self.user_info)


        self.horizontalLayout_7.addWidget(self.user_info_frame)

        self.history_button = QPushButton(self.background_frame)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setGeometry(QRect(30, 70, 100, 25))
        sizePolicy2.setHeightForWidth(self.history_button.sizePolicy().hasHeightForWidth())
        self.history_button.setSizePolicy(sizePolicy2)
        self.history_button.setMinimumSize(QSize(100, 25))
        font5 = QFont()
        font5.setFamilies([u"Rubik"])
        self.history_button.setFont(font5)
        self.history_button.setStyleSheet(u"background: rgba(147, 192, 89, 1);\n"
"color: #281F10;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tare_button.setDefault(False)
        self.units_button.setDefault(False)
        self.new_record_button.setDefault(False)


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
        self.tare_button.setText(QCoreApplication.translate("MainWindow", u"Tara", None))
        self.units_button.setText(QCoreApplication.translate("MainWindow", u"Unidades", None))
        self.new_record_button.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.user_icon.setText("")
        self.user_email_label.setText(QCoreApplication.translate("MainWindow", u"example@user.com", None))
        self.user_gruop_label.setText(QCoreApplication.translate("MainWindow", u"example group", None))
        self.history_button.setText(QCoreApplication.translate("MainWindow", u"Ver historial", None))
    # retranslateUi

