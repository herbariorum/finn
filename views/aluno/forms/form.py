from qt_core import *
import qtawesome as qta
import os 
from datetime import datetime
import json

from views.compenentes.CLabelEdit import CLabelEdit
from views.compenentes.CComboBox import CComboBox
from views.compenentes.CSearch import Form as FormularioDeBusca

import controller.AlunoController as alunoController    # pega os dados dos alunos
import controller.ResponsavelController as responsavelController # para pegar o nome dos pais

from pyUFbr.baseuf import ufbr
from pycpfcnpj import cpf
from libs.uteis import Uteis

base_dir = QDir.currentPath()

class Form(QDialog):

    def __init__(self, tipo, id=None):
        super().__init__()
        
        self.rowID = id
        self.rowIDPai = None
        self.rowIDMae = None
        self.foto_name = None

        self.setWindowTitle(u'Edita/Insere')
        self.setStyleSheet("background-color: #ffffff;")
        self.resize(663, 543)       

        self.initGui()
        
        # verifica o tipo de formulario: Edit ou New
        self.tipo = tipo
        if self.tipo == 'New':
            self.newForm()
        elif self.tipo == 'Edit':
            self.preencheForm()

    def initGui(self):
        self.verticalLayout_1 = QVBoxLayout(self)

        # cria uma linha
        self.frame_1 = QFrame(self)   
        self.frame_1.setFixedHeight(100)     
        self.hLayout_01 = QHBoxLayout(self.frame_1)

        # Foto
        self.frameFoto = QFrame(self.frame_1)
        self.frameFoto.setStyleSheet("background-color: red;")
        self.hLayout_foto = QHBoxLayout(self.frameFoto)

        # https://doc.qt.io/qtforpython/examples/example_multimedia__camera.html
        self.labelFoto = QLabel(self.frameFoto)
        iconFoto = qta.icon("fa.camera")  
        self.labelFoto.setPixmap(iconFoto.pixmap(QSize(64, 64)))
        self.labelFoto.setFixedSize(QSize(70, 70))
        self.labelFoto.mousePressEvent = self.upload_foto
        self.hLayout_foto.addWidget(self.labelFoto)

        self.hLayout_01.addWidget(self.frameFoto)
        # -- Foto

        self.lineEditNome = CLabelEdit(self.frame_1)
        self.lineEditNome.setObjectName(u"nome_txt")
        self.lineEditNome.setFixedHeight(48)
        self.lineEditNome.setLabelText("Nome")
        self.hLayout_01.addWidget(self.lineEditNome)

        self.lineEditCPF = CLabelEdit(self.frame_1)
        self.lineEditCPF.setObjectName(u"cpf_txt")
        self.lineEditCPF.setFixedHeight(48)
        self.lineEditCPF.setFixedWidth(150)
        self.lineEditCPF.setLabelText('CPF')
        self.lineEditCPF.lineEdit.setInputMask("000.000.000-00")
        # self.lineEditCPF.setFixedWidth(150)
        self.hLayout_01.addWidget(self.lineEditCPF)
    
        self.verticalLayout_1.addWidget(self.frame_1)
    
        self.frame_2 = QFrame(self)
        self.hLayout_02 = QHBoxLayout(self.frame_2)

        self.lineEditNascimento = CLabelEdit(self.frame_2)
        self.lineEditNascimento.setObjectName(u"nascimento_txt")
        self.lineEditNascimento.setFixedHeight(48)
        self.lineEditNascimento.setLabelText("Data Nascimento")
        self.lineEditNascimento.lineEdit.setInputMask("00/00/0000")
        self.hLayout_02.addWidget(self.lineEditNascimento)        

        self.cbxSexo = CComboBox(self.frame_2)
        self.cbxSexo.setLabelText(u"Sexo")
        self.cbxSexo.setItems(["Selecione", "MASCULINO", "FEMININO"])
        self.cbxSexo.setFixedHeight(48)
        self.hLayout_02.addWidget(self.cbxSexo)

        #identidade, orgao e uf
        self.lineEditRG = CLabelEdit(self.frame_2)
        self.lineEditRG.setObjectName(u"rg_txt")
        self.lineEditRG.setFixedHeight(48)
        self.lineEditRG.setLabelText("Identidade")
        # self.lineEditRG.setFixedWidth(120)
        self.hLayout_02.addWidget(self.lineEditRG)

        self.lineEditOrgaoExp = CLabelEdit(self.frame_2)
        self.lineEditOrgaoExp.setObjectName(u"orgao_exp_txt")
        self.lineEditOrgaoExp.setFixedHeight(48)
        self.lineEditOrgaoExp.setLabelText("Órgão Expedidor")
        # self.lineEditOrgaoExp.setFixedWidth(200)
        self.hLayout_02.addWidget(self.lineEditOrgaoExp)

        self.cbxUF_Exp = CComboBox(self.frame_2)
        self.cbxUF_Exp.setLabelText(u"UF")
        self.cbxUF_Exp.setItems(ufbr.list_uf)
        self.cbxUF_Exp.setFixedHeight(48)
        self.hLayout_02.addWidget(self.cbxUF_Exp)

        self.verticalLayout_1.addWidget(self.frame_2)

        
        # dados da naturalidade e nacionalidade       
        self.frame_nat = QFrame(self)
        self.hLayout_nat = QHBoxLayout(self.frame_nat)

        self.uf_naturalidade = CComboBox(self.frame_nat)
        self.uf_naturalidade.setLabelText(u"UF")
        self.uf_naturalidade.setItems(ufbr.list_uf)
        self.uf_naturalidade.setFixedHeight(48)
        self.uf_naturalidade.combo.currentTextChanged.connect(self.on_cidade_naturalidade_changed)
        self.hLayout_nat.addWidget(self.uf_naturalidade)

        self.naturalidade = CComboBox(self.frame_nat)
        self.naturalidade.setLabelText(u"Naturalidade")
        self.naturalidade.setFixedHeight(48)  
           
        self.hLayout_nat.addWidget(self.naturalidade)
        
        self.nacionalidade = CComboBox(self.frame_nat)
        self.nacionalidade.setLabelText(u"Naturalidade")
        self.naturalidade.setFixedHeight(48)        
        self.hLayout_nat.addWidget(self.nacionalidade)

        self.verticalLayout_1.addWidget(self.frame_nat)

        # dados da certidao de nascimento
        # certidao_nascimento, termo_certidao_nasc, folha_certidao_nasc
        # livro_certidao_nasc , data_emissao_certidao, cartorio_certidao
        self.frame_certidao = QFrame(self)
        self.hLayout_certidao = QHBoxLayout(self.frame_certidao)

        self.certidao = CLabelEdit(self.frame_certidao)
        self.certidao.setFixedHeight(48)
        self.certidao.setLabelText('Certidão de Nascimento')
        self.hLayout_certidao.addWidget(self.certidao)

        self.termo_certidao = CLabelEdit(self.frame_certidao)
        self.termo_certidao.setFixedHeight(48)
        self.termo_certidao.setLabelText('Termo')
        self.hLayout_certidao.addWidget(self.termo_certidao)

        self.folha_certidao = CLabelEdit(self.frame_certidao)
        self.folha_certidao.setFixedHeight(48)
        self.folha_certidao.setLabelText('Folha')
        self.hLayout_certidao.addWidget(self.folha_certidao)

        self.livro_certidao = CLabelEdit(self.frame_certidao)
        self.livro_certidao.setFixedHeight(48)
        self.livro_certidao.setLabelText('Livro')
        self.hLayout_certidao.addWidget(self.livro_certidao)

        self.verticalLayout_1.addWidget(self.frame_certidao)
        
        # data_emissao_certidao, cartorio_certidao
        self.frame_cartorio = QFrame(self)
        self.hLayout_cartorio = QHBoxLayout(self.frame_cartorio)

        self.cartorio = CLabelEdit(self.frame_cartorio)
        self.cartorio.setFixedHeight(48)
        self.cartorio.setLabelText("Cartório de emissão")
        self.hLayout_cartorio.addWidget(self.cartorio)

        self.emissao_certidao = CLabelEdit(self.frame_cartorio)
        self.emissao_certidao.setFixedHeight(48)
        self.emissao_certidao.setFixedWidth(120)
        self.emissao_certidao.setLabelText("Data Certidão")
        self.emissao_certidao.lineEdit.setInputMask('00/00/0000')
        self.hLayout_cartorio.addWidget(self.emissao_certidao)

        self.verticalLayout_1.addWidget(self.frame_cartorio)

        # informa os pais ou responsável do aluno
        self.frame_3 = QFrame(self)

        self.hLayout_03 = QHBoxLayout(self.frame_3)

        self.lineEditPai = CLabelEdit(self.frame_3)
        self.lineEditPai.setObjectName(u"nome_pai")
        self.lineEditPai.setFixedHeight(48)
        self.lineEditPai.setLabelText("Nome do Pai/Responsável")
        self.lineEditPai.setEnabled(False)
        # self.lineEditPai.setFixedWidth(200)
        self.hLayout_03.addWidget(self.lineEditPai)

        self.button_Busca_Pai = QPushButton(self.frame_3)
        self.button_Busca_Pai.setObjectName(u"btnPai")
        self.button_Busca_Pai.setIcon(qta.icon("fa.ellipsis-h", color="black"))
        self.button_Busca_Pai.setFixedSize(QSize(32, 32))
        self.button_Busca_Pai.setStyleSheet(
            """
            #btnPai {background-color: green;   }  
            QToolTip { color: #ffffff; background-color: #000000; border: 0px; }       
            """
        )
        self.button_Busca_Pai.setToolTip("Localizar pai")
        self.button_Busca_Pai.clicked.connect(self.pegar_nome_pai)
        self.hLayout_03.addWidget(self.button_Busca_Pai)

        self.lineEditMae = CLabelEdit(self.frame_3)
        self.lineEditMae.setObjectName(u"nome_mae")
        self.lineEditMae.setFixedHeight(48)
        self.lineEditMae.setLabelText("Nome da Mâe/Responsável")
        self.lineEditMae.setEnabled(False)
        # self.lineEditOrgaoExp.setFixedWidth(200)
        self.hLayout_03.addWidget(self.lineEditMae)

        self.button_Busca_Mae = QPushButton(self.frame_3)
        self.button_Busca_Mae.setObjectName(u"btnMae")
        self.button_Busca_Mae.setIcon(qta.icon("fa.ellipsis-h", color="black"))
        self.button_Busca_Mae.setFixedSize(QSize(32, 32))
        self.button_Busca_Mae.setStyleSheet(
            """
            #btnMae {background-color: green;  }  
            QToolTip { color: #ffffff; background-color: #000000; border: 0px; }          
            """
        )
        self.button_Busca_Mae.setToolTip("Localiza mãe")
        self.button_Busca_Mae.clicked.connect(self.pegar_nome_mae)
        self.hLayout_03.addWidget(self.button_Busca_Mae)

        self.verticalLayout_1.addWidget(self.frame_3)
        # quarta linha
        self.frame_4 = QFrame(self)
        self.hLayout_04 = QHBoxLayout(self.frame_4)

        self.lineEditEndereco = CLabelEdit(self.frame_4)
        self.lineEditEndereco.setObjectName(u"endereco_txt")
        self.lineEditEndereco.setFixedHeight(48)
        self.lineEditEndereco.setLabelText("Endereço")
        self.hLayout_04.addWidget(self.lineEditEndereco)

        self.verticalLayout_1.addWidget(self.frame_4)

        self.frame_5 = QFrame(self)
        self.hLayout_05 = QHBoxLayout(self.frame_5)
        # estado cidade, bairro
        self.cbxEstado = CComboBox(self.frame_5)
        self.cbxEstado.setLabelText("UF")
        self.cbxEstado.setFixedHeight(48)
        self.cbxEstado.setItems(ufbr.list_uf) 
        self.cbxEstado.combo.currentTextChanged.connect(self.on_combo_estado_changed)
        self.hLayout_05.addWidget(self.cbxEstado)

        self.cbxCidade = CComboBox(self.frame_5)
        self.cbxCidade.setLabelText("Cidade")
        self.cbxCidade.setFixedHeight(48)
        # self.cbxCidade.setItems(["Selecione", "Augustinópolis"])
        self.hLayout_05.addWidget(self.cbxCidade)

        self.lineEditBairro = CLabelEdit(self.frame_4)
        self.lineEditBairro.setObjectName(u"bairro_txt")
        self.lineEditBairro.setFixedHeight(48)
        self.lineEditBairro.setLabelText("Bairro")
        self.hLayout_04.addWidget(self.lineEditBairro)

        self.verticalLayout_1.addWidget(self.frame_5)

        # botões de cancel e ok
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.verificarRegistros)
        self.buttonBox.rejected.connect(self.reject)

        self.verticalLayout_1.addWidget(self.buttonBox)

    def preence_cbx_naturalidade(self):
        self.nacionalidade.combo.clear()
        lista = []
        with open(base_dir +'/static/json/ListaPaises.json') as paises:
            data = json.load(paises)            
            for i in range(len(data)):
                lista.append(data[i]['nome'])
                
        self.nacionalidade.setItems(lista)
        self.nacionalidade.setText('Brasil')

    def on_cidade_naturalidade_changed(self):
        estado = self.uf_naturalidade.getText()
        if estado:
            self.naturalidade.combo.clear()
            self.naturalidade.setItems(ufbr.list_cidades(estado))
        

    def on_combo_estado_changed(self):
        estado = self.cbxEstado.getText()
        if estado:
            self.cbxCidade.combo.clear()
            self.cbxCidade.setItems(ufbr.list_cidades(estado))
        else:
            return

    def newForm(self):
        self.foto_name = None
        self.lineEditNome.setText('')
        self.lineEditCPF.setText('')

        self.lineEditNascimento.setText('')
        self.cbxSexo.setText('MASCULINO')
        self.lineEditRG.setText('')
        self.lineEditOrgaoExp.setText('')
        self.cbxUF_Exp.setText('TO')        

        self.preence_cbx_naturalidade()  
        self.uf_naturalidade.setText('TO')
        # self.naturalidade.setText('')
        self.nacionalidade.setText('Brasil')

        self.certidao.setText('')
        self.termo_certidao.setText('') 
        self.folha_certidao.setText('')
        self.livro_certidao.setText('')
        
        self.cartorio.setText('')  
        self.emissao_certidao.setText('')

        self.lineEditPai.setText('')
        self.lineEditMae.setText('')

        self.lineEditEndereco.setText('')
        self.lineEditBairro.setText('')
        self.cbxEstado.setText('TO')
        self.cbxCidade.setText('')

    def preencheForm(self):
        row = alunoController.selectById(self.rowID)
        if row.photo:
            path_base = os.getcwd()                 
            foto = os.path.join(path_base+'/' , row.photo.decode('UTF-8'))  
            self.foto_name = foto      
            self.exibe_foto(foto)
        self.lineEditNome.setText(row.nome)
        self.lineEditCPF.setText(row.cpf)
        self.lineEditRG.setText(row.rg)
        self.cbxSexo.setText(row.sexo)    
        self.lineEditNascimento.setText(row.nascimento.strftime("%d/%m/%Y")) 
        self.lineEditOrgaoExp.setText(row.orgao_exp_rg)
        self.cbxUF_Exp.setText(row.uf_exp_rg)

        self.preence_cbx_naturalidade()  
        self.uf_naturalidade.setText(row.uf_naturalidade)
        self.naturalidade.setText(row.naturalidade)
        self.nacionalidade.setText(row.nacionalidade)

        self.certidao.setText(row.certidao_nascimento)
        self.termo_certidao.setText(row.termo_certidao_nasc)
        self.folha_certidao.setText(row.folha_certidao_nasc)
        self.livro_certidao.setText(row.livro_certidao_nasc)

        self.cartorio.setText(row.cartorio_certidao)
        self.emissao_certidao.setText(row.data_emissao_certidao)

        pai = self.buscaPais(row.pai)
        self.rowIDPai = row.pai
        self.lineEditPai.setText(pai)
        mae = self.buscaPais(row.mae)
        self.rowIDMae = row.mae
        self.lineEditMae.setText(mae)

        self.lineEditEndereco.setText(row.endereco)
        self.lineEditBairro.setText(row.bairro)
        self.cbxEstado.setText(row.uf)
        self.cbxCidade.setText(row.cidade)

    def upload_foto(self, event):
        fname = QFileDialog.getOpenFileName(self, 'Open file', QDir.currentPath(), "*.png")
        
        if not len(fname[0]) == 0:
            self.exibe_foto(fname[0])
            self.foto_name = fname[0]     

    def exibe_foto(self, fname):        
        if fname:                       
            self.foto_icon = QIcon(fname)
            self.labelFoto.setPixmap(self.foto_icon.pixmap(QSize(64, 64)))

    def saveImage(self, filename):
        file = QFile(filename)
        if not file.open(QIODevice.ReadOnly):
            return
        name = self.pega_nome_foto(filename)
                
        image = QImage()
        image.load(filename,"PNG")
        image.save('static/uploads/'+name, "PNG", -1)
    
    def pega_nome_foto(self, filename):
        file = QFile(filename)
        if not file.open(QIODevice.ReadOnly):
            return
        name = QFileInfo(filename).fileName()
        return name

    def buscaPais(self, id):
        row = responsavelController.selectById(id)
        return row.nome

    def pegar_nome_pai(self):
        # retorna o id e nome do pai
        colunas = ['ID', 'NOME', 'CPF']
        dlg = FormularioDeBusca(responsavelController, colunas,'MASCULINO')
        ret = dlg.exec()
        if ret == 1:
            # print(dlg.rowID, dlg.rowValue)
            self.lineEditPai.setText(dlg.rowValue)
            self.rowIDPai = dlg.rowID
    

    def pegar_nome_mae(self):
        # retorna o id e nome da mae
        colunas = ['ID', 'NOME', 'CPF']
        dlg = FormularioDeBusca(responsavelController, colunas,  'FEMININO')
        ret = dlg.exec()
        if ret == 1:
            self.lineEditMae.setText(dlg.rowValue)
            self.rowIDMae = dlg.rowID


    def verificarRegistros(self):      
        nome = self.lineEditNome.text()
        ccpf = Uteis.is_only_number(self.lineEditCPF.text())
        rg = Uteis.is_only_number(self.lineEditRG.text())
        orgao_exp_rg = self.lineEditOrgaoExp.text()
        uf_exp_rg = self.cbxUF_Exp.getText()
        nascimento = datetime.strptime(self.lineEditNascimento.text(), '%d/%m/%Y').date()
        sexo = self.cbxSexo.getText()
        pai = self.rowIDPai
        mae = self.rowIDMae
        endereco = self.lineEditEndereco.text()
        cidade = self.cbxCidade.getText()
        bairro = self.lineEditBairro.text()
        uf = self.cbxEstado.getText()

        uf_naturalidade = self.uf_naturalidade.getText()
        naturalidade = self.naturalidade.getText()
        nacionalidade = self.nacionalidade.getText()
        certidao_nascimento = self.certidao.text()
        termo_certidao = self.termo_certidao.text()
        folha_certidao = self.folha_certidao.text()
        livro_certidao = self.livro_certidao.text()
        data_emissao_certidao = self.emissao_certidao.text()
        cartorio = self.cartorio.text()

        checkCpfValido = cpf.validate(ccpf) 

        if not checkCpfValido:
            QMessageBox.about(self, 'Aviso', 'Digite um CPF válido')
            return 

        values = {}
        values['nome'] = nome
        values['cpf'] = ccpf
        values['rg'] = rg if rg else '0000000'
        values['orgao_exp_rg'] = orgao_exp_rg
        values['uf_exp_rg'] = uf_exp_rg
        values['nascimento'] = nascimento
        values['sexo'] = sexo
        values['pai'] = pai if pai else 0
        values['mae'] = mae if mae else 1
        values['endereco'] = endereco
        values['cidade'] = cidade 
        values['bairro'] = bairro
        values['uf'] = uf
        values['uf_naturalidade'] = uf_naturalidade
        values['naturalidade'] = naturalidade
        values['nacionalidade'] = nacionalidade
        values['certidao_nascimento'] = certidao_nascimento
        values['termo_certidao_nasc'] = termo_certidao
        values['folha_certidao_nasc'] = folha_certidao
        values['livro_certidao_nasc'] = livro_certidao
        values['data_emissao_certidao'] = data_emissao_certidao
        values['cartorio_certidao'] = cartorio
                
        if not self.rowID:
            # novo registro
            retorno = alunoController.verificaCPFExiste(ccpf)
            if not retorno:
                if self.foto_name:
                    values['photo'] = 'static/uploads/'+self.pega_nome_foto(self.foto_name)    
                else:
                    values['photo'] = 'static/uploads/sample.jpg'            
                r = alunoController.insert(values) # retorna int ou erro                
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
            # atualiza registro
            values['atualizadoem'] = datetime.today().date()
            values['id'] = self.rowID
            
            if self.foto_name:
                values['photo'] = 'static/uploads/'+self.pega_nome_foto(self.foto_name)
            else:
                values['photo'] = 'static/uploads/sample.jpg'
            r = alunoController.update(values) # retorna um int ou um erro (ValueErro)
            if type(r) == ValueError or type(r) == TypeError:
                QMessageBox.warning(self, 'Erro', str(r), QMessageBox.Ok)
                return
            else:
                self.saveImage(self.foto_name)
                QMessageBox.about(self, 'Sucesso', 'Registro atualizado com sucesso.')
        self.accept()