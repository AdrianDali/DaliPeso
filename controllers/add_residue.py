import sys
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton, QComboBox, QLabel
from interface.Ui_add_residue import Ui_add_residue as Ui_MainWindow
from interface.general_custom_ui import GeneralCustomUi
from api.add_residue import add_residue


class AddResidueForm(QWidget,Ui_MainWindow):
    def __init__(self, id_report=None, donor=None):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        residues = ["PET", "HDPE", "PVC", "LDPE", "PP", "PS"]
        self.residues_comboBox.addItems(residues)
        self.donor = donor
        self.id_report = id_report
        self.id_label.setText(self.id_report)
        self.add_button.clicked.connect(self.add_residue_report)
    
    def add_residue_report(self):
        residue = self.residues_comboBox.currentText()
        peso = float(self.weight_label.text())
        try:
            response = add_residue(self.donor, self.id_report, residue, peso)
            self.result_label.setText("Se agregó correctamente")
            print(response)
        except Exception as e:
            self.result_label.setText("Ocurrió un error")
            print(e)

        