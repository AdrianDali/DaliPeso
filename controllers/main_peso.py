from os import access
from PySide6.QtWidgets import QWidget
from controllers.login import LoginForm
from interface.Ui_main_peso import Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.weighing_units import WeighingUnitsForm
from PySide6.QtWidgets import  QGraphicsEllipseItem,QWidget,QGraphicsView, QTableWidgetItem,QAbstractItemView, QHBoxLayout, QFrame,QSizePolicy
from controllers.create_record import CreateRecordForm
from database.SQLite import DatabaseManager
from controllers.history_record import HistoryRecordForm

class MainPesoForm(QWidget,Ui_MainWindow):
    def config_table(self):


        column_labels = ("ID", "NOMBRE REGISTRO",
        "PESO", "DESCRICION", "FECHA", "HORA",
        )
        
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
        self.weighing_units = WeighingUnitsForm()
        self.weighing_units.show()


    def openMenuLogin(self):
        win = LoginForm()
        win.show()

    def openMenuCreateRecord(self):
        win = CreateRecordForm(db_manager=self.db_manager)
        win.record_saved.connect(self.load_table_data)
        win.show()

    def openMenuHistoryRecord(self):
        win = HistoryRecordForm( db_manager=self.db_manager)
        win.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.loginMenu = LoginForm(parent=self)
        self.accessToken = None
        self.refreshToken = None
        self.user = None
        self.checkAuth()
        self.config_table()
        self.db_manager = DatabaseManager()
        self.db_manager.initialize_db()
        self.load_table_data()
        # self.set_table_data()

        self.new_recipe_button_6.clicked.connect(self.menuWeighingUnits)
        self.new_recipe_button_2.clicked.connect(self.openMenuLogin)
        self.new_recipe_button_7.clicked.connect(self.openMenuCreateRecord)
        self.new_recipe_button_2.clicked.connect(self.authButtonClicked)
        self.view_button.clicked.connect(self.openMenuHistoryRecord)
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
            
    def load_table_data(self):
        records = self.db_manager.get_records()
        self.registro_table.setRowCount(len(records))

        for row_idx, row_data in enumerate(records):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.registro_table.setItem(row_idx, col_idx, item)