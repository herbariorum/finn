from qt_core import *

import controller.ResponsavelController as responsavelController
from views.pages.compenentes.ui_responsalvelEditor import Ui_Dialog

class ResponsavelDialog(QDialog):
    def __init__(self, tipo, id=None):
        super().__init__()

        self.IdToEdit = id
  
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        if tipo == 'New':
            self.newForm()
        elif tipo == 'Edit':
            self.preencheForm()
            
    
    def preencheForm(self):
        retorno = responsavelController.selectById(self.IdToEdit)
        for row in retorno:
            self.ui.lblID.setText(str(row.id))
            self.ui.txtNome.setText(row.nome)
            self.ui.txtCPF.setText(row.cpf)
            self.ui.txtEmail.setText(row.email)
            self.ui.cbxSexo.setCurrentText(row.sexo)
           
            self.ui.cbxTipoResponsavel.setCurrentText(row.tipo_responsavel)
            self.ui.txtProfissao.setText(row.profissao)
            #busca os endereços cadastrados de acordo com o ID
            self.ui.lblEndereco.setText('Rua são martins')
            #busca os contatos cadastrados para o id
            self.ui.lblContato.setText('63 99933-3333')
            if row.status == 0:
                self.ui.chbAtivo.setChecked(True)
            elif row.status == 1:
                self.ui.chbAtivo.setChecked(False)

    
    def newForm(self):
        self.ui.lblID.setText('NoNo')
        self.ui.txtNome.setText('')
        self.ui.txtCPF.setText('')
        self.ui.txtCPF.setMask('000.000.000-00')
        self.ui.txtEmail.setText('')
        self.ui.cbxSexo.setCurrentText('MASCULINO')
        self.ui.cbxTipoResponsavel.setCurrentText('PAI')
        self.ui.txtProfissao.setText('')
            #busca os endereços cadastrados de acordo com o ID
        self.ui.lblEndereco.setText('')
            #busca os contatos cadastrados para o id
        self.ui.lblContato.setText('')
        self.ui.chbAtivo.setChecked(False)