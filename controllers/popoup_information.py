import sys
from PyQt5.QtWidgets import QApplication, QWidget
from interface.Ui_popoup_information import Ui_DetailWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.weighing_units import WeighingUnitsForm

class Popoup_infomrationForm(QWidget,Ui_DetailWindow):
    
    def menuWeighingUnits(self):
        self.weighing_units = WeighingUnitsForm()
        self.weighing_units.show()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        # self.config_table()
        # self.set_table_data()

        self.new_recipe_button_6.clicked.connect(self.menuWeighingUnits)
        # self.new_recipe_button_3.clicked.connect(self.machine_menu)
        # self.new_recipe_button_4.clicked.connect(self.part_menu)
        # self.view_button.clicked.connect(self.view_recipe)
        
    