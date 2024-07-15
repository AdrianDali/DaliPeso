from PySide6.QtWidgets import QWidget
from interface.general_custom_ui import GeneralCustomUi
from interface.Ui_warning_dialog import Ui_warning_dialog


class WarningDialog(QWidget, Ui_warning_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.acceptButton.clicked.connect(self.close)