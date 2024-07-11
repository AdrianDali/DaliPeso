# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/errorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(359, 240)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 361, 242))
        self.frame.setObjectName("frame")
        self.background_frame = QtWidgets.QFrame(self.frame)
        self.background_frame.setEnabled(True)
        self.background_frame.setGeometry(QtCore.QRect(10, 10, 341, 222))
        self.background_frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.background_frame.setStyleSheet("background-color: rgb(218, 232, 202);\n"
"border: 0;\n"
"border-radius: 5px;")
        self.background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.background_frame.setObjectName("background_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar_frame = QtWidgets.QFrame(self.background_frame)
        self.top_bar_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.top_bar_frame.setStyleSheet("background-color: #dc2626;\n"
"border-radius: 5px;")
        self.top_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar_frame.setObjectName("top_bar_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.top_bar_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.close_button = QtWidgets.QToolButton(self.frame_3)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.maximize_button = QtWidgets.QToolButton(self.frame_3)
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_2.addWidget(self.maximize_button)
        self.minimize_button = QtWidgets.QToolButton(self.frame_3)
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_2.addWidget(self.minimize_button)
        self.restore_button = QtWidgets.QToolButton(self.frame_3)
        self.restore_button.setObjectName("restore_button")
        self.horizontalLayout_2.addWidget(self.restore_button)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.top_bar_frame)
        self.frame_4 = QtWidgets.QFrame(self.background_frame)
        self.frame_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_4.setStyleSheet("border: 0;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.message = QtWidgets.QLabel(self.frame_4)
        self.message.setAutoFillBackground(False)
        self.message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.message.setWordWrap(False)
        self.message.setObjectName("message")
        self.horizontalLayout_3.addWidget(self.message)
        self.icon = QtWidgets.QLabel(self.frame_4)
        self.icon.setMaximumSize(QtCore.QSize(80, 16777215))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("ui_files/assets/error_icon.svg"))
        self.icon.setObjectName("icon")
        self.horizontalLayout_3.addWidget(self.icon)
        self.verticalLayout.addWidget(self.frame_4)
        self.acceptButton = QtWidgets.QPushButton(self.background_frame)
        self.acceptButton.setMinimumSize(QtCore.QSize(100, 30))
        self.acceptButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.acceptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acceptButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.acceptButton.setStyleSheet("background-color: rgb(0, 143, 0);\n"
"padding: 4 16;\n"
"border-radius: 5px;\n"
"color: white;")
        self.acceptButton.setObjectName("acceptButton")
        self.verticalLayout.addWidget(self.acceptButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.close_button.setText(_translate("Dialog", "..."))
        self.maximize_button.setText(_translate("Dialog", "..."))
        self.minimize_button.setText(_translate("Dialog", "..."))
        self.restore_button.setText(_translate("Dialog", "..."))
        self.label.setText(_translate("Dialog", "Error"))
        self.message.setText(_translate("Dialog", "khbcdfkvbdfbvkdfjhbvkdfbv"))
        self.acceptButton.setText(_translate("Dialog", "Aceptar"))
