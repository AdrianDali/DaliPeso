import sys
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton, QComboBox, QLabel
from interface.Ui_weighing_units import Ui_DetailWindow as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi


class WeighingUnitsForm(QWidget,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.initUI()
        
    def unidades(self):
        print("Unidades", self.unidades_comboBox.currentText())
        unidad = self.unidades_comboBox.currentText()
        if unidad == "Onzas":
            self.result_label.setText("Onzas")
        elif unidad == "Libras":
            self.result_label.setText("Libras")
        elif unidad == "Kilos":
            self.result_label.setText("Kilos")
        else:
            self.result_label.setText("No se ha seleccionado ninguna unidad")
        
    
    def initUI(self):
        self.unidades_button = self.findChild(QPushButton, "unidades_button")
        self.unidades_comboBox = self.findChild(QComboBox, "unidades_comboBox")
        self.unidades_button.clicked.connect(self.unidades)
        self.result_label = self.findChild(QLabel, "result_label")  # Ajusta el nombre según tu archivo .ui

        unidades = ["Onzas", "Libras", "Kilos"]
        self.unidades_comboBox.addItems(unidades)