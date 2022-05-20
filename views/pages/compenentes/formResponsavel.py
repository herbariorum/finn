from qt_core import *

import controller.ResponsavelController as responsavelController
from views.pages.compenentes.ui_responsalvelEditor import Ui_Dialog

from libs.uteis import Uteis
from pycpfcnpj import cpf

import os

class ResponsavelDialog(QDialog):
    def __init__(self, tipo, id=None):
        super().__init__()

        self.IdToEdit = id
        self.foto_name = None
  
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.tipo = tipo
        if self.tipo == 'New':
            self.newForm()
        elif self.tipo == 'Edit':
            self.preencheForm()
        
        self.ui.buttonBox.accepted.connect(self.verificarRegistros)
        self.ui.txtCPF.setInputMask('999.999.999-99')
        self.ui.txtContato.setInputMask('(99)99999-9999')
        self.ui.txtContato.setToolTip('Insira um telefone para contato. \nEx. (63)00202-20202')
        self.ui.lblFoto.mousePressEvent = self.upload_foto
            
            
    def upload_foto(self, event):
        fname = QFileDialog.getOpenFileName(self, 'Open file', QDir.currentPath(), "*.png")
        if not len(fname[0]) == 0:
            self.exibe_foto(fname[0])
            self.foto_name = fname[0]
        
            
    def saveImage(self, filename):
        file = QFile(filename)
        if not file.open(QIODevice.ReadOnly):
            return
        name = self.pega_nome_foto(filename)
                
        image = QImage()
        image.load(filename,"PNG")
        image.save('static/uploads/'+name, "PNG", -1)

    def exibe_foto(self, fname):        
        if fname:                       
            self.foto_icon = QIcon(fname)
            self.ui.lblFoto.setPixmap(self.foto_icon.pixmap(QSize(64, 64)))

    def pega_nome_foto(self, filename):
        file = QFile(filename)
        if not file.open(QIODevice.ReadOnly):
            return
        name = QFileInfo(filename).fileName()
        return name
        
    def verificarRegistros(self):
        id = self.ui.lblID.text()
        nome = self.ui.txtNome.text()
        cpff = self.ui.txtCPF.text()
        email = self.ui.txtEmail.text()
        profissao = self.ui.txtProfissao.text()
        endereco = self.ui.txtEndereco.text()
        contato = self.ui.txtContato.text()
        responsavel = self.ui.cbxTipoResponsavel.currentText()
        sexo = self.ui.cbxSexo.currentText()
        if self.ui.chbAtivo.isChecked():
            status = 0
        else:
            status = 1

        checkID = Uteis.is_not_blank(id)
        checkNome = Uteis.is_not_blank(nome)    
        checkCpfValido = cpf.validate(cpff)       
        checkEmail = Uteis.check_email(email)
        checkProfissao = Uteis.is_not_blank(profissao)
        checkEndereco = Uteis.is_not_blank(endereco)
        checkContato = Uteis.is_not_blank(contato)
        if not checkNome:
            QMessageBox.about(self, 'Aviso', 'O campo nome não pode está em vazio')
            return    
        if not checkCpfValido:
            QMessageBox.about(self, 'Aviso', 'Digite um CPF válido')
            return 
        if not checkEmail:
            QMessageBox.about(self, 'Aviso', 'Digite um Email válido')
            return
        if not checkProfissao:
            QMessageBox.about(self, 'Aviso', 'O campo profissão não pode está vazio')
            return
        if not checkEndereco:
            QMessageBox.about(self, 'Aviso', 'O campo profissão não pode está vazio')
            return
        if not checkContato:
            QMessageBox.about(self, 'Aviso', 'Por favor, forneça pelo menos um telefone de contato')
            return
        
        values = {}
        values['nome'] = nome
        values['cpf'] = Uteis.is_only_number(cpff)
        values['sexo'] = sexo
        values['email'] = email
        values['tipo_responsavel'] = responsavel
        values['profissao'] = profissao
        values['contatos'] = Uteis.is_only_number(contato)
        values['endereco'] = endereco
        values['status'] = status

   
        if not checkID:
            retorno = responsavelController.verificaCPFExiste(Uteis.is_only_number(cpff))
            if not retorno:    
                if self.foto_name:
                    values['photo'] = 'static/uploads/'+self.pega_nome_foto(self.foto_name)       
                r = responsavelController.insert(values)  # retorna um int ou um erro
                if type(r) == ValueError or type(r) == TypeError:
                    QMessageBox.warning(self, 'Erro', str(r), QMessageBox.Ok)
                    return
                else:
                    self.saveImage(self.foto_name)
                    QMessageBox.about(self, 'Sucesso', 'Registro criado com sucesso.')        
            else:
                QMessageBox.about(self, 'Aviso', 'O CPF já está cadastro na base de dados.')
                return
        else:                     
            values['id'] = id
            # adicionar a data atual
            values['atualizadoem'] = datetime.today().date()
            if self.foto_name:
                values['photo'] = 'static/uploads/'+self.pega_nome_foto(self.foto_name)
            r = responsavelController.update(values) # retorna um int ou um erro (ValueErro)
            if type(r) == ValueError or type(r) == TypeError:
                QMessageBox.warning(self, 'Erro', str(r), QMessageBox.Ok)
                return
            else:
                self.saveImage(self.foto_name)
                QMessageBox.about(self, 'Sucesso', 'Registro atualizado com sucesso.')
        self.accept()
    
    

    def preencheForm(self):
        row = responsavelController.selectById(self.IdToEdit)           
        if row.photo:
            path_base = os.getcwd()        
            foto = os.path.join(path_base+'/' , row.photo)        
            self.exibe_foto(foto)
            
        self.ui.lblID.setText(str(row.id))
        self.ui.txtNome.setText(row.nome)
        self.ui.txtCPF.setText(row.cpf)
        self.ui.txtEmail.setText(row.email)
        self.ui.cbxSexo.setCurrentText(row.sexo)           
        self.ui.cbxTipoResponsavel.setCurrentText(row.tipo_responsavel)
        self.ui.txtProfissao.setText(row.profissao)
            #busca os endereços cadastrados de acordo com o ID
        self.ui.txtEndereco.setText(row.endereco)
            #busca os contatos cadastrados para o id
        self.ui.txtContato.setText(row.contatos)
        if row.status == 0:
            self.ui.chbAtivo.setChecked(True)
        elif row.status == 1:
            self.ui.chbAtivo.setChecked(False)

    
    def newForm(self):
        self.ui.lblID.setText('')
        self.ui.txtNome.setText('')
        self.ui.txtCPF.setText('')
        self.ui.txtEmail.setText('')
        self.ui.cbxSexo.setCurrentText('MASCULINO')
        self.ui.cbxTipoResponsavel.setCurrentText('PAI')
        self.ui.txtProfissao.setText('')
            #busca os endereços cadastrados de acordo com o ID
        self.ui.txtEndereco.setText('')
            #busca os contatos cadastrados para o id
        self.ui.txtContato.setText('')
        self.ui.chbAtivo.setChecked(True)