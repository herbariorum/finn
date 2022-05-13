from qt_core import *

import controller.ResponsavelController as responsavelController
from views.pages.compenentes.ui_responsavelView import Ui_Dialog
import os

class ViewResponsavelDialog(QDialog):
    def __init__(self, id):
        super().__init__()

        self.rowID = id
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.limpaForm()
        self.carregaForm()
        self.estilizar()
        self.ui.pushButton.clicked.connect(self.sair)
        self.ui.infoFoto.setFrameShape(QFrame.NoFrame)
        self.ui.infoFoto.setFrameShadow(QFrame.Raised)
        self.ui.frame.setFrameShape(QFrame.NoFrame)
        self.ui.frame.setFrameShadow(QFrame.Raised)
        

    
    def sair(self):
        self.close()
        
    def estilizar(self):
        style = """
            # background-color: cyan;
            padding: 10px;
            color: black;
            font-weight: 600;
            """
        style1 = """
            font-weight: 900;
        
            """
        self.ui.label.setStyleSheet(style)
        self.ui.label_2.setStyleSheet(style)
        self.ui.label_3.setStyleSheet(style)
        self.ui.label_4.setStyleSheet(style)
        self.ui.label_5.setStyleSheet(style)
        self.ui.label_6.setStyleSheet(style)
        self.ui.label_7.setStyleSheet(style)
        self.ui.label_9.setStyleSheet(style)

        self.ui.infoNome.setStyleSheet(style1)
        self.ui.infoContato.setStyleSheet(style1)
        self.ui.infoCPF.setStyleSheet(style1)
        self.ui.infoEmail.setStyleSheet(style1)
        self.ui.infoEndereco.setStyleSheet(style1)
        self.ui.infoResponsavel.setStyleSheet(style1)
        self.ui.infoSexo.setStyleSheet(style1)
        self.ui.infoProfissao.setStyleSheet(style1)
    
    def limpaForm(self):
        self.ui.infoNome.setText('')
        self.ui.infoContato.setText('')
        self.ui.infoCPF.setText('')
        self.ui.infoEmail.setText('')
        self.ui.infoEndereco.setText('')
        self.ui.infoResponsavel.setText('')
        self.ui.infoSexo.setText('')
        self.ui.infoProfissao.setText('')

    def carregaForm(self):
        row = responsavelController.selectById(self.rowID)

        if row.photo:
            path_base = os.getcwd()        
            foto = os.path.join(path_base+'/' , row.photo)        
           
            self.foto_icon = QIcon(foto)
            self.ui.lblFoto.setPixmap(self.foto_icon.pixmap(QSize(64, 64)))
        self.ui.infoNome.setText(row.nome)
        self.ui.infoContato.setText(row.contatos)
        self.ui.infoCPF.setText(row.cpf)
        self.ui.infoEmail.setText(row.email)
        self.ui.infoEndereco.setText(row.endereco)
        self.ui.infoResponsavel.setText(row.tipo_responsavel)
        self.ui.infoSexo.setText(row.sexo)
        self.ui.infoProfissao.setText(row.profissao)