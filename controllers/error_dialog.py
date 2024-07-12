from PyQt5.QtWidgets import QWidget
from interface.general_custom_ui import GeneralCustomUi
from interface.error_dialog import Ui_Dialog


class ErrorDialog(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.acceptButton.clicked.connect(self.close)