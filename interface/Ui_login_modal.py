# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)
from . import recursos_rc

class Ui_login_modal(object):
    def setupUi(self, login_modal):
        if not login_modal.objectName():
            login_modal.setObjectName(u"login_modal")
        login_modal.resize(280, 338)
        login_modal.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(login_modal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(login_modal)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(218, 232, 202);")
        self.background_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.content_frame.setStyleSheet(u"border-radius: 5px;")
        self.content_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: #4d705b;")
        self.top_bar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setSpacing(0)
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
        self.buttons_holder_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_holder_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        icon = QIcon()
        icon.addFile(u"../../../../../pys6-recipes-organizer/assets/icons/close-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_button.setIcon(icon)
        self.restore_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.restore_button)

        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setIcon(icon)
        self.maximize_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.maximize_button)

        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.minimize_button)

        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(0, 8))
        icon1 = QIcon(QIcon.fromTheme(u"x-office-spreadsheet"))
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.close_button)


        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.user_icon = QLabel(self.content_frame)
        self.user_icon.setObjectName(u"user_icon")
        self.user_icon.setPixmap(QPixmap(u":/iconos/assets/icons/user_icon.svg"))
        self.user_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.user_icon)

        self.email = QVBoxLayout()
        self.email.setSpacing(4)
        self.email.setObjectName(u"email")
        self.email.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.email_label = QLabel(self.content_frame)
        self.email_label.setObjectName(u"email_label")

        self.email.addWidget(self.email_label)

        self.email_field = QLineEdit(self.content_frame)
        self.email_field.setObjectName(u"email_field")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_field.sizePolicy().hasHeightForWidth())
        self.email_field.setSizePolicy(sizePolicy)
        self.email_field.setMinimumSize(QSize(230, 0))
        self.email_field.setStyleSheet(u"background-color: #fff;\n"
"border: 1px solid rgba(5, 84, 29, 176);\n"
"")

        self.email.addWidget(self.email_field)


        self.verticalLayout_2.addLayout(self.email)

        self.password = QVBoxLayout()
        self.password.setSpacing(4)
        self.password.setObjectName(u"password")
        self.password.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.password_label = QLabel(self.content_frame)
        self.password_label.setObjectName(u"password_label")

        self.password.addWidget(self.password_label)

        self.password_field = QLineEdit(self.content_frame)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setMinimumSize(QSize(230, 0))
        self.password_field.setStyleSheet(u"background-color: #fff;\n"
"border: 1px solid rgba(5, 84, 29, 176);\n"
"")
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.password.addWidget(self.password_field)


        self.verticalLayout_2.addLayout(self.password)

        self.buttons = QHBoxLayout()
        self.buttons.setObjectName(u"buttons")
        self.buttons.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.send_button = QPushButton(self.content_frame)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setMaximumSize(QSize(100, 16777215))
        self.send_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.send_button.setStyleSheet(u"background-color: rgb(0, 143, 0);\n"
"padding: 4 16;\n"
"border-radius: 5px;\n"
"color: white;")

        self.buttons.addWidget(self.send_button)


        self.verticalLayout_2.addLayout(self.buttons)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(login_modal)

        QMetaObject.connectSlotsByName(login_modal)
    # setupUi

    def retranslateUi(self, login_modal):
        login_modal.setWindowTitle(QCoreApplication.translate("login_modal", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("login_modal", u"Iniciar sesi\u00f3n", None))
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.minimize_button.setText("")
        self.close_button.setText("")
        self.user_icon.setText("")
        self.email_label.setText(QCoreApplication.translate("login_modal", u"Correo electr\u00f3nico", None))
        self.email_field.setPlaceholderText(QCoreApplication.translate("login_modal", u"ejemplo@correo.com", None))
        self.password_label.setText(QCoreApplication.translate("login_modal", u"Contrase\u00f1a", None))
        self.password_field.setPlaceholderText(QCoreApplication.translate("login_modal", u"********", None))
        self.send_button.setText(QCoreApplication.translate("login_modal", u"Enviar", None))
    # retranslateUi

