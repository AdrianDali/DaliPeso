# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_record.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)
from . import resources_rc

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
        self.background_frame.setStyleSheet(u"background: #F9F6EE;\n"
"border-radius: 5px;")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.background_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 40))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background: #93C059;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 4, 0)
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(False)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white;")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.buttons_holder_frame = QFrame(self.top_bar_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(0, 30))
        self.buttons_holder_frame.setMaximumSize(QSize(113, 16777215))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_holder_frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/iconos/assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon)
        self.maximize_button.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.maximize_button)

        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.restore_button)

        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon2)
        self.minimize_button.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.minimize_button)

        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/iconos/assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.close_button)


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
        self.horizontalSpacer_7 = QSpacerItem(93, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.descripcion_label = QLabel(self.gridLayoutWidget)
        self.descripcion_label.setObjectName(u"descripcion_label")
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(13)
        font1.setBold(False)
        self.descripcion_label.setFont(font1)
        self.descripcion_label.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}")
        self.descripcion_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.descripcion_label, 3, 0, 1, 1)

        self.registro_line_edit = QLineEdit(self.gridLayoutWidget)
        self.registro_line_edit.setObjectName(u"registro_line_edit")
        self.registro_line_edit.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setBold(False)
        self.registro_line_edit.setFont(font2)
        self.registro_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #4d705b;")

        self.gridLayout.addWidget(self.registro_line_edit, 2, 1, 1, 2)

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

        self.gridLayout.addWidget(self.result_label, 4, 1, 1, 2)

        self.descripcion_line_edit = QLineEdit(self.gridLayoutWidget)
        self.descripcion_line_edit.setObjectName(u"descripcion_line_edit")
        self.descripcion_line_edit.setMinimumSize(QSize(0, 30))
        self.descripcion_line_edit.setFont(font2)
        self.descripcion_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #4d705b;")

        self.gridLayout.addWidget(self.descripcion_line_edit, 3, 1, 1, 2)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 5, 0, 1, 1)

        self.peso_label = QLabel(self.gridLayoutWidget)
        self.peso_label.setObjectName(u"peso_label")
        font3 = QFont()
        font3.setFamilies([u"Rubik"])
        font3.setPointSize(20)
        font3.setBold(False)
        self.peso_label.setFont(font3)
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

        self.gridLayout.addWidget(self.registro_nombre_label, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 5, 3, 1, 1)

        self.guardar_registro_button = QPushButton(self.gridLayoutWidget)
        self.guardar_registro_button.setObjectName(u"guardar_registro_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guardar_registro_button.sizePolicy().hasHeightForWidth())
        self.guardar_registro_button.setSizePolicy(sizePolicy)
        self.guardar_registro_button.setMinimumSize(QSize(30, 30))
        self.guardar_registro_button.setMaximumSize(QSize(302, 40))
        font4 = QFont()
        font4.setFamilies([u"Rubik"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.guardar_registro_button.setFont(font4)
        self.guardar_registro_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.guardar_registro_button.setLayoutDirection(Qt.LeftToRight)
        self.guardar_registro_button.setStyleSheet(u"background-color: rgb(0, 143, 0);\n"
"padding: 4 16;\n"
"border-radius: 5px;\n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"../../../../PyAdministracion/pys6-recipes-organizer/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.guardar_registro_button.setIcon(icon4)
        self.guardar_registro_button.setIconSize(QSize(28, 45))

        self.gridLayout.addWidget(self.guardar_registro_button, 5, 1, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 3, 1, 1)

        self.unit = QLabel(self.gridLayoutWidget)
        self.unit.setObjectName(u"unit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.unit.sizePolicy().hasHeightForWidth())
        self.unit.setSizePolicy(sizePolicy1)
        self.unit.setMinimumSize(QSize(300, 0))
        self.unit.setMaximumSize(QSize(300, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Orbitron"])
        font5.setPointSize(64)
        font5.setBold(True)
        self.unit.setFont(font5)
        self.unit.setStyleSheet(u"margin: 0px;\n"
"color: #281F10;")
        self.unit.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.unit, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamilies([u"Rubik"])
        font6.setPointSize(40)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"color: #281F10;")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(DetailWindow)

        QMetaObject.connectSlotsByName(DetailWindow)
    # setupUi

    def retranslateUi(self, DetailWindow):
        DetailWindow.setWindowTitle(QCoreApplication.translate("DetailWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("DetailWindow", u"Nuevo registro", None))
        self.maximize_button.setText("")
        self.restore_button.setText("")
        self.minimize_button.setText("")
        self.close_button.setText("")
        self.descripcion_label.setText(QCoreApplication.translate("DetailWindow", u"Descripcion:", None))
        self.result_label.setText("")
        self.peso_label.setText(QCoreApplication.translate("DetailWindow", u"Peso:", None))
        self.registro_nombre_label.setText(QCoreApplication.translate("DetailWindow", u"Nombre del registro:", None))
        self.guardar_registro_button.setText(QCoreApplication.translate("DetailWindow", u"Guardar", None))
        self.unit.setText(QCoreApplication.translate("DetailWindow", u"000.0", None))
        self.label.setText(QCoreApplication.translate("DetailWindow", u"g", None))
    # retranslateUi

