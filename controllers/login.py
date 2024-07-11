

from PySide6.QtGui import QCloseEvent, QShowEvent
from PySide6.QtWidgets import QWidget
from interface.general_custom_ui import GeneralCustomUi
from interface.login import Ui_login_modal
from api.login import login
from controllers.error_dialog import ErrorDialog



class LoginForm(QWidget,Ui_login_modal):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.parent = parent
        self.send_button.clicked.connect(self.authenticate)
        self.errorDialog = ErrorDialog()
        

    def authenticate(self):
        try:
            request = {
                "username": self.email_field.text(),
                "password": self.password_field.text()
            }
            response = login(request)
            self.parent.accessToken = response["access"]
            self.parent.refreshToken = response["refresh"]
            self.parent.user = request["username"]
            #self.parent.new_recipe_button_2.setText("Cerrar sesión")
            self.close()
        except Exception as e:
            print(e)
            self.errorDialog.show()
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.parent.checkAuth()
        self.email_field.clear()
        self.password_field.clear()
        return super().closeEvent(event)
    
    def showEvent(self, event: QShowEvent) -> None:
        self.email_field.setFocus()
        return super().showEvent(event)
    
    