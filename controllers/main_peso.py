from os import access
from PyQt5.QtWidgets import QWidget, QGraphicsEllipseItem, QGraphicsView, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame, QSizePolicy, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal as Signal, QThread
from controllers.login import LoginForm

from interface.Ui_main_window import Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.weighing_units import WeighingUnitsForm
from controllers.create_record import CreateRecordForm
from database.SQLite import DatabaseManager
from controllers.history_record import HistoryRecordForm
from controllers.warning_dialog import WarningDialog
from PyQt5.QtGui import QMouseEvent
from api.read_user import read_user
from PyQt5.QtWidgets import QMainWindow

#from hardware.worker import WeightReader

class MainPesoForm(QMainWindow, Ui_MainWindow):
    def config_table(self):
        column_labels = ("ID", "NOMBRE REGISTRO", "PESO", "DESCRICION", "FECHA", "HORA")
        
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

    def openMenuCreateRecord(self):
        win = CreateRecordForm(db_manager=self.db_manager)
        win.record_saved.connect(self.load_table_data)
        win.show()
        self.weight_reader.weight_updated.connect(win.update_weight_label)


    def openMenuHistoryRecord(self):
        win = HistoryRecordForm(db_manager=self.db_manager)
        win.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.loginMenu = LoginForm(parent=self)
        self.accessToken = None
        self.refreshToken = None
        self.user = None
        self.logOutConfirmation = WarningDialog()
        self.checkAuth()
        self.config_table()
        self.db_manager = DatabaseManager()
        self.db_manager.initialize_db()
        self.load_table_data()
        self.user_info_frame.mousePressEvent = self.logout

        self.units_button.clicked.connect(self.menuWeighingUnits)
        self.new_record_button.clicked.connect(self.openMenuCreateRecord)
        self.login_button.clicked.connect(self.authButtonClicked)
        self.history_button.clicked.connect(self.openMenuHistoryRecord)

        # Inicializar el WeightReader y conectar la señal
        # self.weight_reader = WeightReader()
        # self.weight_reader_thread = QThread()
        # self.weight_reader.moveToThread(self.weight_reader_thread)
        # self.weight_reader_thread.started.connect(self.weight_reader.read_weight)
        # self.weight_reader.weight_updated.connect(self.update_weight_label)
        # self.weight_reader_thread.start()

    def authButtonClicked(self):
        if self.accessToken is None:
            self.loginMenu.show()
        else:
            self.accessToken = None
            self.refreshToken = None
            self.user = None
            self.checkAuth()

    def checkAuth(self):
        if self.accessToken is None:
            self.login_button.setVisible(True)
            self.user_info_frame.setVisible(False)
        else:
            self.login_button.setVisible(False)
            self.user_info_frame.setVisible(True)
            try:
                self.user = read_user(self.user)
                self.user_email_label.setText(self.user["email"])
                self.user_gruop_label.setText(self.user["groups"][0])
            except Exception as e:
                print(e)
                self.accessToken = None
                self.refreshToken = None
                self.user = None
                self.checkAuth()
            
    def load_table_data(self):
        records = self.db_manager.get_records()
        self.registro_table.setRowCount(len(records))

        for row_idx, row_data in enumerate(records):
            for col_idx, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.registro_table.setItem(row_idx, col_idx, item)
    
    def update_weight_label(self, weight):
        self.unit.setText(f"{weight:.2f} ")
    
   #@Slot()
    def logout(self, event: QMouseEvent):
        self.logOutConfirmation.show()
        self.logOutConfirmation.message.setText("¿Está seguro que deseas cerrar sesión?")
        self.logOutConfirmation.acceptButton.clicked.connect(self.authButtonClicked)
