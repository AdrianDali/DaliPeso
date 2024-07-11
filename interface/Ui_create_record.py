# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_record.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_DetailWindow(object):
    def setupUi(self, DetailWindow):
        if not DetailWindow.objectName():
            DetailWindow.setObjectName(u"DetailWindow")
        DetailWindow.resize(693, 443)
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
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 621, 321))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.descripcion_line_edit = QLineEdit(self.gridLayoutWidget)
        self.descripcion_line_edit.setObjectName(u"descripcion_line_edit")
        self.descripcion_line_edit.setMinimumSize(QSize(0, 30))
        self.descripcion_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #4d705b;")

        self.gridLayout.addWidget(self.descripcion_line_edit, 2, 1, 1, 2)

        self.peso_line_edit = QLineEdit(self.gridLayoutWidget)
        self.peso_line_edit.setObjectName(u"peso_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peso_line_edit.sizePolicy().hasHeightForWidth())
        self.peso_line_edit.setSizePolicy(sizePolicy)
        self.peso_line_edit.setMinimumSize(QSize(0, 30))
        self.peso_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #4d705b;")

        self.gridLayout.addWidget(self.peso_line_edit, 0, 1, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 4, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 4, 3, 1, 1)

        self.guardar_registro_button = QPushButton(self.gridLayoutWidget)
        self.guardar_registro_button.setObjectName(u"guardar_registro_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.guardar_registro_button.sizePolicy().hasHeightForWidth())
        self.guardar_registro_button.setSizePolicy(sizePolicy1)
        self.guardar_registro_button.setMinimumSize(QSize(30, 30))
        self.guardar_registro_button.setMaximumSize(QSize(302, 40))
        self.guardar_registro_button.setFont(font)
        self.guardar_registro_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.guardar_registro_button.setLayoutDirection(Qt.LeftToRight)
        self.guardar_registro_button.setStyleSheet(u"QPushButton{\n"
"	background-color : #328f62;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon4 = QIcon()
        icon4.addFile(u"../../../../PyAdministracion/pys6-recipes-organizer/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.guardar_registro_button.setIcon(icon4)
        self.guardar_registro_button.setIconSize(QSize(28, 45))

        self.gridLayout.addWidget(self.guardar_registro_button, 4, 1, 1, 2)

        self.registro_line_edit = QLineEdit(self.gridLayoutWidget)
        self.registro_line_edit.setObjectName(u"registro_line_edit")
        self.registro_line_edit.setMinimumSize(QSize(0, 30))
        self.registro_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #4d705b;")

        self.gridLayout.addWidget(self.registro_line_edit, 1, 1, 1, 2)

        self.descripcion_label = QLabel(self.gridLayoutWidget)
        self.descripcion_label.setObjectName(u"descripcion_label")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.descripcion_label.setFont(font1)
        self.descripcion_label.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.descripcion_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.descripcion_label, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 3, 1, 1)

        self.peso_label = QLabel(self.gridLayoutWidget)
        self.peso_label.setObjectName(u"peso_label")
        self.peso_label.setFont(font1)
        self.peso_label.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.peso_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.peso_label, 0, 0, 1, 1)

        self.registro_nombre_label = QLabel(self.gridLayoutWidget)
        self.registro_nombre_label.setObjectName(u"registro_nombre_label")
        self.registro_nombre_label.setFont(font1)
        self.registro_nombre_label.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.registro_nombre_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.registro_nombre_label, 1, 0, 1, 1)

        self.result_label = QLabel(self.gridLayoutWidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setEnabled(False)
        self.result_label.setMaximumSize(QSize(300, 20))
        self.result_label.setStyleSheet(u"QLabel {\n"
"    color: red;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result_label, 3, 1, 1, 2)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("DetailWindow", u"Creacion de registro", None))
        self.minimize_button.setText("")
        self.restore_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.guardar_registro_button.setText(QCoreApplication.translate("DetailWindow", u"Guardar", None))
        self.descripcion_label.setText(QCoreApplication.translate("DetailWindow", u"Descripcion:", None))
        self.peso_label.setText(QCoreApplication.translate("DetailWindow", u"Peso:", None))
        self.registro_nombre_label.setText(QCoreApplication.translate("DetailWindow", u"Nombre del registro:", None))
        self.result_label.setText("")
    # retranslateUi

