# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_login_modal(object):
    def setupUi(self, login_modal):
        login_modal.setObjectName("login_modal")
        login_modal.resize(280, 304)
        login_modal.setStyleSheet("border-radius: 5px;")
        self.verticalLayout = QtWidgets.QVBoxLayout(login_modal)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.central_widget_frame = QtWidgets.QFrame(login_modal)
        self.central_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_widget_frame.setObjectName("central_widget_frame")
        self.shadow_layout = QtWidgets.QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName("shadow_layout")
        self.background_frame = QtWidgets.QFrame(self.central_widget_frame)
        self.background_frame.setStyleSheet("background-color: rgb(218, 232, 202);")
        self.background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame.setObjectName("background_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.content_frame = QtWidgets.QFrame(self.background_frame)
        self.content_frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_bar_frame = QtWidgets.QFrame(self.content_frame)
        self.top_bar_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet("background-color: #4d705b;")
        self.top_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar_frame.setObjectName("top_bar_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.title_label = QtWidgets.QLabel(self.top_bar_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_3.addWidget(self.title_label)
        self.buttons_holder_frame = QtWidgets.QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QtCore.QSize(110, 16777215))
        self.buttons_holder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_holder_frame.setObjectName("buttons_holder_frame")
        self.close_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.close_button.setGeometry(QtCore.QRect(90, 0, 21, 22))
        self.close_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_files/../../../../../pys6-recipes-organizer/assets/icons/close-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QtCore.QSize(25, 25))
        self.close_button.setObjectName("close_button")
        self.minimize_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.minimize_button.setGeometry(QtCore.QRect(60, 0, 21, 22))
        self.minimize_button.setText("")
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QtCore.QSize(25, 25))
        self.minimize_button.setObjectName("minimize_button")
        self.maximize_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.maximize_button.setGeometry(QtCore.QRect(20, 0, 21, 22))
        self.maximize_button.setText("")
        self.maximize_button.setIcon(icon)
        self.maximize_button.setIconSize(QtCore.QSize(25, 25))
        self.maximize_button.setObjectName("maximize_button")
        self.restore_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.restore_button.setGeometry(QtCore.QRect(10, 10, 21, 22))
        self.restore_button.setText("")
        self.restore_button.setIcon(icon)
        self.restore_button.setIconSize(QtCore.QSize(25, 25))
        self.restore_button.setObjectName("restore_button")
        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)
        self.verticalLayout_2.addWidget(self.top_bar_frame)
        self.user_icon = QtWidgets.QLabel(self.content_frame)
        self.user_icon.setText("")
        self.user_icon.setPixmap(QtGui.QPixmap("ui_files/assets/user_icon.svg"))
        self.user_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.user_icon.setObjectName("user_icon")
        self.verticalLayout_2.addWidget(self.user_icon)
        self.email = QtWidgets.QVBoxLayout()
        self.email.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.email.setSpacing(4)
        self.email.setObjectName("email")
        self.email_label = QtWidgets.QLabel(self.content_frame)
        self.email_label.setObjectName("email_label")
        self.email.addWidget(self.email_label)
        self.email_field = QtWidgets.QLineEdit(self.content_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_field.sizePolicy().hasHeightForWidth())
        self.email_field.setSizePolicy(sizePolicy)
        self.email_field.setMinimumSize(QtCore.QSize(230, 0))
        self.email_field.setStyleSheet("background-color: #fff;\n"
"border: 1px solid rgba(5, 84, 29, 176);\n"
"")
        self.email_field.setObjectName("email_field")
        self.email.addWidget(self.email_field)
        self.verticalLayout_2.addLayout(self.email)
        self.password = QtWidgets.QVBoxLayout()
        self.password.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.password.setSpacing(4)
        self.password.setObjectName("password")
        self.password_label = QtWidgets.QLabel(self.content_frame)
        self.password_label.setObjectName("password_label")
        self.password.addWidget(self.password_label)
        self.password_field = QtWidgets.QLineEdit(self.content_frame)
        self.password_field.setMinimumSize(QtCore.QSize(230, 0))
        self.password_field.setStyleSheet("background-color: #fff;\n"
"border: 1px solid rgba(5, 84, 29, 176);\n"
"")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.password.addWidget(self.password_field)
        self.verticalLayout_2.addLayout(self.password)
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.buttons.setObjectName("buttons")
        self.send_button = QtWidgets.QPushButton(self.content_frame)
        self.send_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.send_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.send_button.setStyleSheet("background-color: rgb(0, 143, 0);\n"
"padding: 4 16;\n"
"border-radious: 5px;\n"
"color: white;")
        self.send_button.setObjectName("send_button")
        self.buttons.addWidget(self.send_button)
        self.verticalLayout_2.addLayout(self.buttons)
        self.verticalLayout_3.addWidget(self.content_frame)
        self.shadow_layout.addWidget(self.background_frame)
        self.verticalLayout.addWidget(self.central_widget_frame)

        self.retranslateUi(login_modal)
        QtCore.QMetaObject.connectSlotsByName(login_modal)

    def retranslateUi(self, login_modal):
        _translate = QtCore.QCoreApplication.translate
        login_modal.setWindowTitle(_translate("login_modal", "Form"))
        self.title_label.setText(_translate("login_modal", "Iniciar sesión"))
        self.email_label.setText(_translate("login_modal", "Correo electrónico"))
        self.email_field.setPlaceholderText(_translate("login_modal", "ejemplo@correo.com"))
        self.password_label.setText(_translate("login_modal", "Contraseña"))
        self.password_field.setPlaceholderText(_translate("login_modal", "********"))
        self.send_button.setText(_translate("login_modal", "Enviar"))