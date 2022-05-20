from qt_core import *
import qtawesome as qta
from modelos.CustomTableModel import CustomTableModel

class Form(QDialog):
    def __init__(self, controller, column, value):
        super().__init__()

        self.resize(557, 327)
        self.setWindowTitle('Localizar')

        self.colunas = column

        self.rowID = None
        self.rowValue = None

        self.value = value

        self.controller = controller
        self.initGui()

   
    def initGui(self):
        vLayout = QVBoxLayout(self)

        # adiciona um frame, o label e a caixa de texto para busca
        frame_1 = QFrame(self)
        frame_1.setFrameShape(QFrame.StyledPanel)
        frame_1.setFrameShadow(QFrame.Raised)

        hLayout = QHBoxLayout(frame_1)
        
        label = QLabel(frame_1)
        hLayout.addWidget(label)

        self.edtLocalizar = QLineEdit(frame_1)
        self.edtLocalizar.setObjectName(u"txt_localizar")
        self.edtLocalizar.addAction(qta.icon('fa.search'), QLineEdit.LeadingPosition)
        self.edtLocalizar.textChanged.connect(self.localizarItem)
        hLayout.addWidget(self.edtLocalizar)

        vLayout.addWidget(frame_1)
        # fim

        # adiciona a listagem
        frame_2 = QFrame(self)
        frame_2.setFrameShape(QFrame.NoFrame)
        frame_2.setFrameShadow(QFrame.Raised)

        vLayout_2 = QVBoxLayout(frame_2)
        self.tblListagem = QTableView(frame_2)
        dados = self.controller.selectBySexo(self.value)
        self.loadTable(dados)

        vLayout_2.addWidget(self.tblListagem)

        vLayout.addWidget(frame_2)
        # fim

        # adiciona botões
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        vLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.save_form)
        self.buttonBox.rejected.connect(self.cancel_form)

    def loadTable(self, dados):  
        rows = dados
        list_data = []
        for row in rows:
            list_data.append(
                (
                 row.id,
                 row.nome,
                 row.cpf if row.cpf else '000.000.000-000', # if ternario                 
                )
            )        
       
        self.model = CustomTableModel(list_data, self.colunas)
        self.tblListagem.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblListagem.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblListagem.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblListagem.setAlternatingRowColors(True)
        self.tblListagem.setModel(self.model)

        self.tblListagem.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tblListagem.horizontalHeader().setStretchLastSection(True)
        self.tblListagem.verticalHeader().hide()

        self.tblListagem.setColumnWidth(0, 50)
        self.tblListagem.setColumnWidth(1, 300)
        self.tblListagem.setColumnWidth(2, 150)        
     

    def save_form(self):
        indexes = self.tblListagem.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.about(self, 'Aviso', 'Selecione um item na tabela')
            return
        else:
            index = self.tblListagem.selectedIndexes()[0]
            idx2 = self.tblListagem.selectedIndexes()[1]        
            id = int(self.tblListagem.model().data(index))
            nome = self.tblListagem.model().data(idx2)

            self.rowID = id
            self.rowValue = nome
          
            self.accept()


    def cancel_form(self):
        self.reject()

    def localizarItem(self):
        retorno = self.controller.searchBySexo(self.edtLocalizar.text(), self.value)
        self.loadTable(retorno)
