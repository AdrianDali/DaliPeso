from os import access
from PySide6.QtWidgets import QWidget
from controllers.login import LoginForm
from interface.Ui_main_peso import Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi


class MainPesoForm(QWidget, Ui_MainWindow):

    

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.loginMenu = LoginForm(parent=self)
        self.accessToken = None
        self.refreshToken = None
        self.user = None
        self.checkAuth()
        # self.config_table()
        # self.set_table_data()

        # self.new_recipe_button.clicked.connect(self.new_recipe)
        self.new_recipe_button_2.clicked.connect(self.authButtonClicked)
        # self.new_recipe_button_3.clicked.connect(self.machine_menu)
        # self.new_recipe_button_4.clicked.connect(self.part_menu)
        # self.view_button.clicked.connect(self.view_recipe)

    def authButtonClicked(self):
        if(self.accessToken is None):
            self.loginMenu.show()
        else:
            self.accessToken = None
            self.refreshToken = None
            self.user = None
            self.checkAuth()

    def checkAuth(self):
        if self.accessToken is None:
            self.new_recipe_button_2.setText("Iniciar sesión")
            self.new_recipe_button_2.setStyleSheet(
                "QPushButton{\n"
                "	background-color : #328f62;\n"
                "	color: white;\n"
                "}\n"
                "QPushButton::hover {background-color : #ffc13b};"
            )
        else:
            self.new_recipe_button_2.setText("Cerrar sesión")
            self.new_recipe_button_2.setStyleSheet(
                "QPushButton{\n"
                "	background-color : #dc2626;\n"
                "	color: white;\n"
                "}\n"
                "QPushButton::hover {background-color : #ffc13b};"
            )
            
