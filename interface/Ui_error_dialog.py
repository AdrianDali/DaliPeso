# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorDialog.ui'
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
from PyQt5.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
from . import recursos_rc

class Ui_error_dialog(object):
    def setupUi(self, error_dialog):
        if not error_dialog.objectName():
            error_dialog.setObjectName(u"error_dialog")
        error_dialog.resize(359, 240)
        self.frame = QFrame(error_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 361, 242))
        self.background_frame = QFrame(self.frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setEnabled(True)
        self.background_frame.setGeometry(QRect(10, 10, 341, 222))
        self.background_frame.setLayoutDirection(Qt.RightToLeft)
        self.background_frame.setStyleSheet(u"background: #F9F6EE;\n"
"border-radius: 5px;\n"
"border: 0;")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.background_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_bar_frame = QFrame(self.background_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_bar_frame.sizePolicy().hasHeightForWidth())
        self.top_bar_frame.setSizePolicy(sizePolicy)
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #dc2626;\n"
"border-radius: 5px;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, -1, 4, -1)
        self.frame_3 = QFrame(self.top_bar_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.close_button = QToolButton(self.frame_3)
        self.close_button.setObjectName(u"close_button")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/icons/close-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.close_button)

        self.maximize_button = QToolButton(self.frame_3)
        self.maximize_button.setObjectName(u"maximize_button")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/icons/maximize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.maximize_button)

        self.minimize_button = QToolButton(self.frame_3)
        self.minimize_button.setObjectName(u"minimize_button")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/assets/icons/minimize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.restore_button = QToolButton(self.frame_3)
        self.restore_button.setObjectName(u"restore_button")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/assets/icons/restore-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_button.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.restore_button)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.top_bar_frame)

        self.frame_4 = QFrame(self.background_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.RightToLeft)
        self.frame_4.setStyleSheet(u"border: 0;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.message = QLabel(self.frame_4)
        self.message.setObjectName(u"message")
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(13)
        self.message.setFont(font1)
        self.message.setAutoFillBackground(False)
        self.message.setTextFormat(Qt.AutoText)
        self.message.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.message.setWordWrap(True)
        self.message.setMargin(8)

        self.horizontalLayout_3.addWidget(self.message)

        self.icon = QLabel(self.frame_4)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(80, 16777215))
        self.icon.setPixmap(QPixmap(u":/iconos/assets/icons/error_icon.svg"))

        self.horizontalLayout_3.addWidget(self.icon)


        self.verticalLayout.addWidget(self.frame_4)

        self.acceptButton = QPushButton(self.background_frame)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setMinimumSize(QSize(100, 30))
        self.acceptButton.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        self.acceptButton.setFont(font2)
        self.acceptButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.acceptButton.setFocusPolicy(Qt.StrongFocus)
        self.acceptButton.setStyleSheet(u"background-color: rgb(0, 143, 0);\n"
"padding: 4 16;\n"
"border-radius: 5px;\n"
"color: white;")

        self.verticalLayout.addWidget(self.acceptButton)


        self.retranslateUi(error_dialog)

        QMetaObject.connectSlotsByName(error_dialog)
    # setupUi

    def retranslateUi(self, error_dialog):
        error_dialog.setWindowTitle(QCoreApplication.translate("error_dialog", u"Dialog", None))
        self.close_button.setText(QCoreApplication.translate("error_dialog", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("error_dialog", u"...", None))
        self.minimize_button.setText(QCoreApplication.translate("error_dialog", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("error_dialog", u"...", None))
        self.label.setText(QCoreApplication.translate("error_dialog", u"Error", None))
        self.message.setText(QCoreApplication.translate("error_dialog", u"Ocurri\u00f3 un error. Intente de nuevo m\u00e1s tarde.", None))
        self.icon.setText("")
        self.acceptButton.setText(QCoreApplication.translate("error_dialog", u"Aceptar", None))
    # retranslateUi

