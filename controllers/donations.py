import sys
from venv import create
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QTableWidgetItem, QAbstractItemView, QTableWidget
from interface.Ui_donations import Ui_donations as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from api.get_donor_reports import get_donor_reports
from controllers.utils.date_formater import date_formater
from controllers.add_residue import AddResidueForm

class Donations(QWidget, Ui_MainWindow):
    
    def config_table(self):
        column_labels = ("ID", "DONADOR", "FECHA")
        self.registro_table.setColumnCount(len(column_labels))
        self.registro_table.setHorizontalHeaderLabels(column_labels)
        self.registro_table.setColumnWidth(1, 200)
        self.registro_table.setColumnWidth(2, 200)
        self.registro_table.setColumnWidth(3, 200)
        self.registro_table.verticalHeader().setDefaultSectionSize(50)
        #self.registro_table.setColumnHidden(0, True)
        self.registro_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    def menuWeighingUnits(self):
        # self.weighing_units = WeighingUnitsForm()
        self.weighing_units.show()

    def __init__(self, creator_user=None):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.registro_table = self.findChild(QTableWidget, "registro_table") 
        self.user = creator_user
        self.add_residue_menu = AddResidueForm()
        self.config_table()
        self.load_table_data() 
        self.registro_table.cellClicked.connect(self.on_table_click)

    def on_table_click(self, row, column):
        item = self.registro_table.item(row, 0)
        itemDonor = self.registro_table.item(row, 1)
        if item is None:
            print("No se selecciono ningun registro")
        else:
            id_report = item.text()
            self.add_residue_menu = AddResidueForm(id_report=id_report, donor=itemDonor.text())
            self.add_residue_menu.show()
            print(f"Se selecciono el registro {id_report}")

    def load_table_data(self):
        if self.user is None:
            return
        data = get_donor_reports(self.user)
        self.registro_table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            item = QTableWidgetItem(str(row_data["id_report"]))
            self.registro_table.setItem(row_idx, 0, item)
            item = QTableWidgetItem(str(row_data["nombre_usuario"]))
            self.registro_table.setItem(row_idx, 1, item)
            item = QTableWidgetItem(str(date_formater(row_data["fecha_inicio_reporte"])))
            self.registro_table.setItem(row_idx, 2, item)
