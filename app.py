import sys
from PySide6.QtWidgets import QApplication
from controllers.main_peso import MainPesoForm

if __name__ == "__main__":
    app = QApplication()  # Pasar sys.argv al constructor de QApplication
    window = MainPesoForm()
    window.show()
    sys.exit(app.exec_())
