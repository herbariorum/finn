
from qt_core import *

import qtawesome as qta
from views.login.ui_login import Ui_Form
from libs.uteis import Uteis
import controller.LoginController as loginController

import sys

class Login(QWidget, Ui_Form):
    global logou
    logou = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(300, 500)
        icon = QIcon(u'static/img/logo.png')
        self.setWindowIcon(icon)
       
        self.btnTitleExit.setFixedWidth(25)
        self.btnVerificar.clicked.connect(self.verificar_login)
        self.btnTitleExit.clicked.connect(self.fechar_janela)

        iconUser = qta.icon("mdi.email-outline")        
        self.txtUsuario.setClearButtonEnabled(True)
        self.txtUsuario.addAction(iconUser, QLineEdit.LeadingPosition)
        self.txtUsuario.setPlaceholderText(u"Entre com o email")
        
        iconKey = qta.icon("mdi.shield-key-outline")
        self.txtPassword.setClearButtonEnabled(True)
        self.txtPassword.addAction(iconKey, QLineEdit.LeadingPosition)
        self.txtPassword.setPlaceholderText(u"Entre com a senha")

        iconLogo = qta.icon('fa.user-circle', color='black')
        self.label.setPixmap(iconLogo.pixmap(QSize(128, 128)))

        iconCheck = qta.icon("fa.check", color="green")
        self.btnVerificar.setIcon(iconCheck)

        self.tentativas = 0

    def verificar_login(self):
        global logou
        usuario = self.txtUsuario.text()
        password = self.txtPassword.text()
        if not Uteis.is_not_blank(usuario) or not Uteis.check(usuario):
            QMessageBox.about(self, 'Aviso', 'Digite um email válido')
            self.txtUsuario.setFocus()
            return
        if not Uteis.is_not_blank(password) or len(password) < 6:
            QMessageBox.about(self, 'Aviso', 'A senha deve conter no mínimo 6 dígitos')
            self.txtPassword.setFocus()
            return
        
        if loginController.validar_usuario(usuario, password):
            logou = True
            self.close()
        else:
            if self.tentativas < 3:
                QMessageBox.about(self, 'Aviso', 'Login ou senha incorretoss')
                self.tentativas += 1
                if self.tentativas == 3:
                    sys.exit(0)

    def fechar_janela(self):
        info = QMessageBox.question(self, 'Confirmação', 'Você realmente deseja sair do aplicativo?', QMessageBox.Yes | QMessageBox.No,)
        if info == QMessageBox.Yes:
            self.close()


def executa():
    global logou

    try:        
        app = QApplication.instance()
        
        if app is None:            
            app = QApplication(sys.argv)
    
        with open('static/css/login.css', 'r') as f:
            style = f.read()
            app.setStyleSheet(style)
        
        janela = Login()
        janela.show()
        app.exec()
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Fechando Janela...")
    except Exception:
        print(sys.exc_info()[1])
    finally:
        return logou
