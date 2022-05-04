from qt_core import *

import qtawesome as qta
from libs.uteis import Uteis
from views.ui_dashobard import Ui_MainWindow

from views.pages.matriculaPage import MatriculaPage
from views.pages.responsavelPage import ResponsavelPage
from views.pages.homePage import HomePage

import sys

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)        
        self.icon = QIcon(u'static/img/logo.png')
        self.setWindowIcon(self.icon)
        self.setWindowTitle(f'Finnance 0.1')
        self.setWindowFlag(Qt.FramelessWindowHint)
        screensize = QScreen.availableGeometry(QApplication.primaryScreen())
        self.setGeometry(screensize)

        # icone do header 
        iconText = qta.icon('ei.chevron-right', color='black')
        self.lblTopIcon.setPixmap(iconText.pixmap(QSize(32, 32)))
        self.lblTopIcon.setFixedWidth(32)
        # texto do header
        # esse texto varia de acordo com o menu selecionado
        self.lblTopTitle.setText('Selecione uma opção no menu ao lado')

        self.listMenu = self.listView
        self.listMenu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.lblIconLogo.setPixmap(self.icon.pixmap(QSize(32, 32)))
        self.configuraMenu()

        # inicializa as pages
        self.homeWdg = HomePage()
        self.matWdg = MatriculaPage()
        self.respWdg = ResponsavelPage()
        self.pages.addWidget(self.homeWdg)
        self.pages.addWidget(self.matWdg)
        self.pages.addWidget(self.respWdg)

        self.pages.setCurrentIndex(0)
 
    
    def configuraMenu(self):
        self.listMenu.setMaximumWidth(250)
        self.listMenu.setSpacing(0)
        self.item = QStandardItemModel()
        iconeMatricula = qta.icon('fa.user', color='black')
        iconeResponsavel = qta.icon('ei.adult', color='black')
        iconeExit = qta.icon('mdi.exit-run', color='black')
        matricula = QStandardItem(iconeMatricula, 'Matricula')
        responsavel = QStandardItem(iconeResponsavel, 'Responsável')
        exit = QStandardItem(iconeExit, 'Sair')
        self.item.appendRow(matricula)
        self.item.appendRow(responsavel)
        self.item.appendRow(exit)
        self.listMenu.setModel(self.item)
        self.listMenu.clicked.connect(self.itemSelecionado)


    def itemSelecionado(self, index):
        row = self.listMenu.currentIndex().row()
       
        if row == 0:
            self.lblTopTitle.setText('Matrícula')            
            self.showPageMatricula()
        elif row == 1:
            self.lblTopTitle.setText('Responsavel')
            self.showPageResponsavel()
        elif row == 2:
            self.fechar_janela()

    def showPageMatricula(self):
        self.pages.setCurrentIndex(1)
        
    def showPageResponsavel(self):
        self.pages.setCurrentIndex(2)
    
    def fechar_janela(self):
        info = QMessageBox.question(self, 'Confirmação', 'Você realmente deseja sair do aplicativo?', QMessageBox.Yes | QMessageBox.No,)
        if info == QMessageBox.Yes:
            self.close()

def executa():
    try:        
        app = QApplication.instance()        
        if app is None:            
            app = QApplication(sys.argv)

        with open('static/css/dashboard.css', 'r') as f:
            style = f.read()
            app.setStyleSheet(style)
        
        janela = MainWindow()
        janela.show()        
        app.exec()
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Fechando Janela...")
    except Exception:
        print(sys.exc_info()[1])
