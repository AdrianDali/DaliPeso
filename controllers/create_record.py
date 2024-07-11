import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel
from interface.Ui_create_record import Ui_DetailWindow as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.weighing_units import WeighingUnitsForm
from PySide6.QtCore import Signal

class CreateRecordForm(QWidget, Ui_MainWindow):
    record_saved = Signal()
    
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.initUI()

    def initUI(self):
        # Crear los widgets
        self.nombre_input = self.findChild(QLineEdit, "registro_line_edit")  # Ajusta el nombre según tu archivo .ui
        self.peso_input = self.findChild(QLineEdit, "peso_line_edit")  # Ajusta el nombre según tu archivo .ui
        self.descripcion_input = self.findChild(QLineEdit, "descripcion_line_edit")  # Ajusta el nombre según tu archivo .ui
        self.submit_button = self.findChild(QPushButton, "guardar_registro_button")  # Ajusta el nombre según tu archivo .ui
        self.result_label = self.findChild(QLabel, "result_label")  # Ajusta el nombre según tu archivo .ui

        self.submit_button.clicked.connect(self.save_record)

    def save_record(self):
        nombre = self.nombre_input.text()
        peso = self.peso_input.text()
        descripcion = self.descripcion_input.text()

        if nombre and peso:
            try:
                peso = float(peso)
                self.db_manager.insert_record(nombre, peso, descripcion)
                self.result_label.setText("Registro guardado exitosamente.")
                self.clear_inputs()
                self.record_saved.emit()
            except ValueError:
                self.result_label.setText("Por favor ingresa un valor numérico para el peso.")
        else:
            self.result_label.setText("Nombre y Peso son campos obligatorios.")

    def clear_inputs(self):
        self.nombre_input.clear()
        self.peso_input.clear()
        self.descripcion_input.clear()
