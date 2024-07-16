# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/donations.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from . import recursos_rc

class Ui_donations(object):
    def setupUi(self, donations):
        donations.setObjectName("donations")
        donations.resize(684, 433)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        donations.setFont(font)
        donations.setStyleSheet("border-radius: 5px")
        self.verticalLayout = QtWidgets.QVBoxLayout(donations)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.central_widget_frame = QtWidgets.QFrame(donations)
        self.central_widget_frame.setStyleSheet("\n"
"border-radius: 5px;")
        self.central_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_widget_frame.setObjectName("central_widget_frame")
        self.shadow_layout = QtWidgets.QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName("shadow_layout")
        self.background_frame = QtWidgets.QFrame(self.central_widget_frame)
        self.background_frame.setStyleSheet("background: #F9F6EE;\n"
"border-radius: 5px;")
        self.background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame.setObjectName("background_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.top_bar_frame = QtWidgets.QFrame(self.background_frame)
        self.top_bar_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet("background: #93C059;\n"
"")
        self.top_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar_frame.setObjectName("top_bar_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.title_label = QtWidgets.QLabel(self.top_bar_frame)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        font.setBold(False)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_3.addWidget(self.title_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.buttons_holder_frame = QtWidgets.QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QtCore.QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_holder_frame.setObjectName("buttons_holder_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttons_holder_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimize_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.minimize_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/assets/icons/restore-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QtCore.QSize(16, 16))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.maximize_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maximize_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/assets/icons/maximize-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize_button.setIcon(icon1)
        self.maximize_button.setIconSize(QtCore.QSize(16, 16))
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout.addWidget(self.maximize_button)
        self.restore_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.restore_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restore_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/assets/icons/minimize-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore_button.setIcon(icon2)
        self.restore_button.setIconSize(QtCore.QSize(16, 16))
        self.restore_button.setObjectName("restore_button")
        self.horizontalLayout.addWidget(self.restore_button)
        self.close_button = QtWidgets.QToolButton(self.buttons_holder_frame)
        self.close_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconos/assets/icons/close-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QtCore.QSize(16, 16))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)
        self.verticalLayout_2.addWidget(self.top_bar_frame)
        self.content_frame = QtWidgets.QFrame(self.background_frame)
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.content_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.registro_table = QtWidgets.QTableWidget(self.frame)
        self.registro_table.setGeometry(QtCore.QRect(0, 10, 621, 321))
        self.registro_table.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.registro_table.setStyleSheet("QTableWidget {\n"
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
        self.registro_table.setObjectName("registro_table")
        self.registro_table.setColumnCount(0)
        self.registro_table.setRowCount(0)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.content_frame)
        self.shadow_layout.addWidget(self.background_frame)
        self.verticalLayout.addWidget(self.central_widget_frame)

        self.retranslateUi(donations)
        QtCore.QMetaObject.connectSlotsByName(donations)

    def retranslateUi(self, donations):
        _translate = QtCore.QCoreApplication.translate
        donations.setWindowTitle(_translate("donations", "Form"))
        self.title_label.setText(_translate("donations", "Donaciones"))
