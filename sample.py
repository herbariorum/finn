from __future__ import unicode_literals
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtWidgets import QMessageBox, QInputDialog, QHBoxLayout
from views.sample import Ui_Form

class Sample(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Sample, self).__init__(parent)
        self.setupUi(self)

        self.loginBtn.clicked.connect(self.login)
        self.btnCancela.clicked.connect(self.fechar)

    def fechar(self):
        self.close()

    def login(self):
        login, ok = QInputDialog.getText(self, 'Login', 'Entre login:')
        if ok:
            password, ok = QInputDialog.getText(self, 'Login', 'Entre senha')
            if ok:
                if not login or not password:
                    QMessageBox.warning(self, 'Login', 'Login ou senha inválidos', QMessageBox.Ok)
                    return
                QMessageBox.information(self, 'Resultado','Login '+ login + ' Senha '+password , QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Sample()
    okno.show()
    okno.move(350, 200)
    sys.exit(app.exec())