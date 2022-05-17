from qt_core import *
import qtawesome as qta
import os 

from views.compenentes.CLabelEdit import CLabelEdit
from views.compenentes.CComboBox import CComboBox
import controller.AlunoController as alunoController

from pyUFbr.baseuf import ufbr

class Form(QDialog):

    def __init__(self, tipo, id=None):
        super().__init__()
        
        self.rowID = id

        self.setWindowTitle(u'Edita/Insere')
        self.setStyleSheet("background-color: #ffffff;")
        self.resize(663, 443)       

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
        self.hLayout_foto.addWidget(self.labelFoto)

        self.hLayout_01.addWidget(self.frameFoto)
        # -- Foto

        self.lineEditNome = CLabelEdit(self.frame_1)
        self.lineEditNome.setObjectName(u"nome_txt")
        self.lineEditNome.setFixedHeight(48)
        self.lineEditNome.setLabelText("Nome")
        # self.lineEditNome.setText("Elias")
        self.hLayout_01.addWidget(self.lineEditNome)
        # insere o edit na linha

        
        self.verticalLayout_1.addWidget(self.frame_1)
       
        self.frame_2 = QFrame(self)

        self.hLayout_02 = QHBoxLayout(self.frame_2)

        self.lineEditCPF = CLabelEdit(self.frame_2)
        self.lineEditCPF.setObjectName(u"cpf_txt")
        self.lineEditCPF.setFixedHeight(48)
        self.lineEditCPF.label.setText("CPF")
        self.lineEditCPF.lineEdit.setInputMask("000.000.000-00")
        # self.lineEditCPF.setFixedWidth(150)
        self.hLayout_02.addWidget(self.lineEditCPF)

        self.lineEditNascimento = CLabelEdit(self.frame_2)
        self.lineEditNascimento.setObjectName(u"nascimento_txt")
        self.lineEditNascimento.setFixedHeight(48)
        self.lineEditNascimento.label.setText("Data Nascimento")
        self.lineEditNascimento.lineEdit.setInputMask("00/00/0000")
        # self.lineEditNascimento.setFixedWidth(110)
        self.hLayout_02.addWidget(self.lineEditNascimento)        
 
        self.cbxSexo = CComboBox(self.frame_2)
        self.cbxSexo.setLabelText(u"Sexo")
        self.cbxSexo.setItems(["Selecione", "MASCULINO", "FEMININO"])
        self.cbxSexo.setFixedHeight(48)
        self.hLayout_02.addWidget(self.cbxSexo)

        self.verticalLayout_1.addWidget(self.frame_2)

        self.frame_3_ = QFrame(self)
        self.hLayout_03_ = QHBoxLayout(self.frame_3_)

        self.lineEditRG = CLabelEdit(self.frame_3_)
        self.lineEditRG.setObjectName(u"rg_txt")
        self.lineEditRG.setFixedHeight(48)
        self.lineEditRG.label.setText("Identidade")
        self.lineEditRG.setFixedWidth(120)
        self.hLayout_03_.addWidget(self.lineEditRG)

        self.lineEditOrgaoExp = CLabelEdit(self.frame_3_)
        self.lineEditOrgaoExp.setObjectName(u"orgao_exp_txt")
        self.lineEditOrgaoExp.setFixedHeight(48)
        self.lineEditOrgaoExp.setLabelText("Órgão Expedidor")
        self.lineEditOrgaoExp.setFixedWidth(200)
        self.hLayout_03_.addWidget(self.lineEditOrgaoExp)

        self.cbxUF_Exp = CComboBox(self.frame_3_)
        self.cbxUF_Exp.setLabelText(u"UF")
        self.cbxUF_Exp.setItems(ufbr.list_uf)
        self.cbxUF_Exp.setFixedHeight(48)
        self.hLayout_03_.addWidget(self.cbxUF_Exp)

        self.verticalLayout_1.addWidget(self.frame_3_)

        self.frame_3 = QFrame(self)

        self.hLayout_03 = QHBoxLayout(self.frame_3)

        self.lineEditPai = CLabelEdit(self.frame_3)
        self.lineEditPai.setObjectName(u"nome_pai")
        self.lineEditPai.setFixedHeight(48)
        self.lineEditPai.setLabelText("Nome do Pai")
        # self.lineEditPai.setFixedWidth(200)
        self.hLayout_03.addWidget(self.lineEditPai)

        self.button_Busca_Pai = QPushButton(self.frame_3)
        self.button_Busca_Pai.setIcon(qta.icon("fa.ellipsis-h", color="black"))
        self.button_Busca_Pai.setFixedSize(QSize(32, 32))
        self.button_Busca_Pai.setStyleSheet(
            """
            background-color: green;            
            """
        )
        self.button_Busca_Pai.setToolTip("Pesquisa por nome do pai")
        self.hLayout_03.addWidget(self.button_Busca_Pai)

        self.lineEditMae = CLabelEdit(self.frame_3)
        self.lineEditMae.setObjectName(u"nome_mae")
        self.lineEditMae.setFixedHeight(48)
        self.lineEditMae.setLabelText("Nome da Mâe")
        # self.lineEditOrgaoExp.setFixedWidth(200)
        self.hLayout_03.addWidget(self.lineEditMae)

        self.button_Busca_Mae = QPushButton(self.frame_3)
        self.button_Busca_Mae.setIcon(qta.icon("fa.ellipsis-h", color="black"))
        self.button_Busca_Mae.setFixedSize(QSize(32, 32))
        self.button_Busca_Mae.setStyleSheet(
            """
            background-color: green;            
            """
        )
        self.button_Busca_Mae.setToolTip("Pesquisa por nome da Mâe")
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
        self.cbxCidade.setItems(["Selecione", "Augustinópolis"])
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

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.verticalLayout_1.addWidget(self.buttonBox)

    def on_combo_estado_changed(self):
        estado = self.cbxEstado.getText()
        if estado:
            self.cbxCidade.combo.clear()
            self.cbxCidade.setItems(ufbr.list_cidades(estado))
        else:
            return

    def newForm(self):
        pass

    def preencheForm(self):
        row = alunoController.selectById(self.rowID)
        if row.photo:
            path_base = os.getcwd()        
            foto = os.path.join(path_base+'/' , row.photo)        
            self.exibe_foto(foto)
        self.lineEditNome.setText(row.nome)
        self.lineEditCPF.setText(row.cpf)
        self.lineEditRG.setText(row.rg)
       
        self.lineEditNascimento.setText(row.nascimento.strftime("%d/%m/%Y"))
        self.cbxSexo.setText(row.sexo)
        self.lineEditOrgaoExp.setText(row.orgao_exp_rg)
        self.cbxUF_Exp.setText(row.uf_exp_rg)
        self.lineEditMae.setText(str(row.mae))
        self.lineEditPai.setText(str(row.pai))
        self.lineEditEndereco.setText(row.endereco)
        self.lineEditBairro.setText(row.bairro)
        self.cbxEstado.setText(row.uf)
        self.cbxCidade.setText(row.cidade)

    
    def exibe_foto(self, fname):        
        if fname:                       
            self.foto_icon = QIcon(fname)
            self.labelFoto.setPixmap(self.foto_icon.pixmap(QSize(64, 64)))