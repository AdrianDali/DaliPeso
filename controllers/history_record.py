import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QTableWidgetItem, QAbstractItemView, QTableWidget
from interface.Ui_history_record import Ui_DetailWindow as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi

class HistoryRecordForm(QWidget, Ui_MainWindow):
    
    def config_table(self):
        column_labels = ("ID", "NOMBRE REGISTRO",
                         "PESO", "DESCRIPCION", "FECHA", "HORA")
        
        self.registro_table.setColumnCount(len(column_labels))
        self.registro_table.setHorizontalHeaderLabels(column_labels)
        self.registro_table.setColumnWidth(1, 200)
        self.registro_table.setColumnWidth(2, 200)
        self.registro_table.setColumnWidth(3, 200)
        self.registro_table.setColumnWidth(4, 200)
        self.registro_table.setColumnWidth(5, 150)
        self.registro_table.setColumnWidth(6, 150)
        self.registro_table.verticalHeader().setDefaultSectionSize(50)
        self.registro_table.setColumnHidden(0, True)
        self.registro_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    def menuWeighingUnits(self):
        # self.weighing_units = WeighingUnitsForm()
        self.weighing_units.show()

    def __init__(self, db_manager=None):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.registro_table = self.findChild(QTableWidget, "registro_table") 
        self.config_table()
        self.db_manager = db_manager
        self.load_table_data() 
        
    def load_table_data(self):
        if self.db_manager is not None:
            records = self.db_manager.get_records()
            self.registro_table.setRowCount(len(records))

            for row_idx, row_data in enumerate(records):
                for col_idx, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.registro_table.setItem(row_idx, col_idx, item)
