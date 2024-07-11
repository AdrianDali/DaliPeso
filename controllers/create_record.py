import sys
from PySide6.QtWidgets import QApplication, QWidget
from interface.Ui_create_record import Ui_DetailWindow as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.weighing_units import WeighingUnitsForm

class CreateRecordForm(QWidget,Ui_MainWindow):
    
    def menuWeighingUnits(self):
        self.weighing_units = WeighingUnitsForm()
        self.weighing_units.show()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        # self.config_table()
        # self.set_table_data()
        
        
        
    