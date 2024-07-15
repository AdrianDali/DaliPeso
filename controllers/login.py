<<<<<<< HEAD


from PyQt5.QtGui import QCloseEvent, QShowEvent
from PyQt5.QtWidgets import QWidget
=======
from PySide6.QtGui import QCloseEvent, QShowEvent
from PySide6.QtWidgets import QWidget
>>>>>>> main
from interface.general_custom_ui import GeneralCustomUi
from interface.Ui_login_modal import Ui_login_modal
from api.login import login
from controllers.error_dialog import ErrorDialog
from controllers.utils.validateEmail import validateEmail




class LoginForm(QWidget,Ui_login_modal):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.parent = parent
        self.send_button.clicked.connect(self.authenticate)
        self.errorDialog = ErrorDialog()
        

    def authenticate(self):
        print("*********** Authenticating... *******+****+")
        try:
            request = {
                "username": self.email_field.text(),
                "password": self.password_field.text()
            }
            
            if(len(request["username"]) < 1):
                raise Exception("El campo de correo electrónico es requerido.")


            if not validateEmail(request["username"]):
                raise Exception("El correo electrónico ingresado no es válido.")

            if(len(request["password"]) < 1):
                raise Exception("El campo de contraseña es requerido.")
            

            response = login(request)
            self.parent.accessToken = response["access"]
            self.parent.refreshToken = response["refresh"]
            self.parent.user = request["username"]
            self.close()
        except KeyError as e:
            self.errorDialog.message.setText("Las credenciales ingresadas no son válidas.")
            self.errorDialog.show()
        except Exception as e:
            self.errorDialog.message.setText("Ocurrió un error desconoicdo al intentar autenticar. Por favor, inténtelo de nuevo.")
            self.errorDialog.show()
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.parent.checkAuth()
        self.email_field.clear()
        self.password_field.clear()
        return super().closeEvent(event)
    
    def showEvent(self, event: QShowEvent) -> None:
        self.email_field.setFocus()
        return super().showEvent(event)
    
    