from PySide6.QtWidgets import QWidget
from interface.general_custom_ui import GeneralCustomUi
from interface.Ui_error_dialog import Ui_error_dialog


class ErrorDialog(QWidget, Ui_error_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.acceptButton.clicked.connect(self.close)