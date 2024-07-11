import sys
from PySide6.QtWidgets import QApplication, QWidget
from interface.Ui_weighing_units import Ui_DetailWindow as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi


class WeighingUnitsForm(QWidget,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        # self.config_table()
        # self.set_table_data()

        #self.new_recipe_button.clicked.connect(self.new_recipe)
        # self.new_recipe_button_3.clicked.connect(self.machine_menu)
        # self.new_recipe_button_4.clicked.connect(self.part_menu)
        # self.view_button.clicked.connect(self.view_recipe)
        
    