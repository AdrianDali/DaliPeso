import sys
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton, QComboBox, QLabel
from interface.Ui_weighing_units import Ui_DetailWindow as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from PyQt5.QtCore import pyqtSignal as Signal

class WeighingUnitsForm(QWidget,Ui_MainWindow):

    unidad_cambiada = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.initUI()
        
    def unidades(self):
        print("Unidades", self.unidades_comboBox.currentText())
        unidad = self.unidades_comboBox.currentText()
        self.unidad_cambiada.emit(unidad)
        if unidad == "Oz":
            self.result_label.setText("Unidades cambiadas a Onzas")
        elif unidad == "Lb":
            self.result_label.setText("Unidades cambiadas a Libras")
        elif unidad == "Kg":
            self.result_label.setText("Unidades cambiadas a Kilos")
        elif unidad == "gr":  
            self.result_label.setText("Unidades cambiadas a Gramos")
        else:
            self.result_label.setText("No se ha seleccionado ninguna unidad")
        
    
    def initUI(self):
        self.unidades_button = self.findChild(QPushButton, "unidades_button")
        self.unidades_comboBox = self.findChild(QComboBox, "unidades_comboBox")
        self.unidades_button.clicked.connect(self.unidades)
        self.result_label = self.findChild(QLabel, "result_label")  # Ajusta el nombre según tu archivo .ui

        unidades = ["Oz", "Lb", "Kg", "gr",]
        self.unidades_comboBox.addItems(unidades)