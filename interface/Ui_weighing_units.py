# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weighing_units.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(602, 325)
        DetailWindow.setStyleSheet(u"border-radius: 5px")
        self.verticalLayout = QVBoxLayout(DetailWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(DetailWindow)
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
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.background_frame)
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
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"../../../PyAdministracion/pys6-recipes-organizer/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"../../../PyAdministracion/pys6-recipes-organizer/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"../../../PyAdministracion/pys6-recipes-organizer/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"../../../PyAdministracion/pys6-recipes-organizer/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 541, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.peso_label = QLabel(self.gridLayoutWidget)
        self.peso_label.setObjectName(u"peso_label")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.peso_label.setFont(font1)
        self.peso_label.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.peso_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.peso_label, 0, 1, 1, 1)

        self.unidades_comboBox = QComboBox(self.gridLayoutWidget)
        self.unidades_comboBox.setObjectName(u"unidades_comboBox")
        self.unidades_comboBox.setMaximumSize(QSize(16777215, 30))
        self.unidades_comboBox.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #4d705b;")

        self.gridLayout.addWidget(self.unidades_comboBox, 0, 2, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.unidades_button = QPushButton(self.gridLayoutWidget)
        self.unidades_button.setObjectName(u"unidades_button")
        self.unidades_button.setMinimumSize(QSize(150, 30))
        self.unidades_button.setMaximumSize(QSize(16777215, 40))
        self.unidades_button.setFont(font)
        self.unidades_button.setStyleSheet(u"QPushButton{\n"
"	background-color : #328f62;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        self.unidades_button.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.unidades_button, 2, 1, 1, 3)

        self.result_label = QLabel(self.gridLayoutWidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setEnabled(False)
        self.result_label.setMaximumSize(QSize(341, 20))
        self.result_label.setStyleSheet(u"QLabel {\n"
"    color: red;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result_label, 1, 1, 1, 3)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("DetailWindow", u"Unidad de Pesaje", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.peso_label.setText(QCoreApplication.translate("DetailWindow", u"Unidades de Pesaje:", None))
        self.unidades_button.setText(QCoreApplication.translate("DetailWindow", u"Guardad Unidades", None))
        self.result_label.setText("")
    # retranslateUi

