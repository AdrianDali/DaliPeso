import sys
from PySide6.QtWidgets import QApplication, QWidget
from controllers.login import LoginForm
from interface.Ui_main_peso import Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.weighing_units import WeighingUnitsForm
from PySide6.QtWidgets import  QGraphicsEllipseItem,QWidget,QGraphicsView, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame,QSizePolicy


class MainPesoForm(QWidget,Ui_MainWindow):
    def config_table(self):


        column_labels = ("ID", "NOMBRE REGISTRO",
        "PESO", "DESCRICION", "FECHA", "HORA",
        "UNIDAD DE PESO", "OBSERVACIONES")
        
        self.recipes_table.setColumnCount(len(column_labels))
        self.recipes_table.setHorizontalHeaderLabels(column_labels)
        self.recipes_table.setColumnWidth(1, 200)
        self.recipes_table.setColumnWidth(2, 200)
        self.recipes_table.setColumnWidth(3, 200)
        self.recipes_table.setColumnWidth(4, 200)
        self.recipes_table.setColumnWidth(5, 200)
        self.recipes_table.setColumnWidth(6, 200)
        self.recipes_table.setColumnWidth(7, 200)
        self.recipes_table.setColumnWidth(8, 200)
        self.recipes_table.verticalHeader().setDefaultSectionSize(50)
        self.recipes_table.setColumnHidden(0, True)
        self.recipes_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    
    def menuWeighingUnits(self):
        self.weighing_units = WeighingUnitsForm()
        self.weighing_units.show()


    def openMenuLogin(self):
        win = LoginForm()
        win.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()
        # self.set_table_data()

        self.new_recipe_button_6.clicked.connect(self.menuWeighingUnits)
        # self.new_recipe_button.clicked.connect(self.new_recipe)
        self.new_recipe_button_2.clicked.connect(self.openMenuLogin)
        # self.new_recipe_button_3.clicked.connect(self.machine_menu)
        # self.new_recipe_button_4.clicked.connect(self.part_menu)
        # self.view_button.clicked.connect(self.view_recipe)
        
    