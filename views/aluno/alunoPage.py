from qt_core import *
import qtawesome as qta

from views.aluno.ui_aluno import Ui_Form
import controller.AlunoController as alunoController
from modelos.CustomTableModel import CustomTableModel

from views.aluno.forms.form import Form


class AlunoPage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        retorno = alunoController.selectAll()  
        self.loadTable(retorno)

        self.txtLocalizar.setClearButtonEnabled(True)
        self.txtLocalizar.addAction(qta.icon('fa.search'), QLineEdit.LeadingPosition)
        self.txtLocalizar.textChanged.connect(self.localizarItem)
        self.btnNovo.clicked.connect(self.openNewItem)
        self.btnNovo.setIcon(qta.icon('msc.new-file', color='black'))
        self.btnEdit.clicked.connect(self.openEditTable)
        self.btnEdit.setIcon(qta.icon('ei.file-edit', color='black'))
        self.btnDelete.clicked.connect(self.deleteItem)
        self.btnDelete.setIcon(qta.icon('mdi.delete', color='black'))
        self.btnSelecao.clicked.connect(self.imprimeSelecao)
        self.btnSelecao.setIcon(qta.icon('fa.print', color='black'))
        self.btnListagem.clicked.connect(self.imprimeTudo)
        self.btnListagem.setIcon(qta.icon('fa.print', color='black'))
        self.tblListagem.doubleClicked.connect(self.exibeItem)

    def localizarItem(self):
        retorno = alunoController.search(self.txtLocalizar.text())
        self.loadTable(retorno)

    def openNewItem(self):        
        form = Form(tipo="New")
        form.exec()

    def openEditTable(self):
        indexes = self.tblListagem.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.about(self, 'Aviso', 'Selecione um item na tabela')
            return
        else:            
            index = self.tblListagem.selectedIndexes()[0]        
            id = int(self.tblListagem.model().data(index))

            form = Form(tipo="Edit", id=id)
            ret = form.exec()
            if ret == QDialog.Accepted:  
                retorno = alunoController.selectAll()               
                self.loadTable(retorno)         
            else:
                pass

    def deleteItem(self):
        pass

    def imprimeSelecao(self):
        pass

    def imprimeTudo(self):
        pass

    def exibeItem(self):
        pass

    def loadTable(self, dados):
        colunas = ['ID', 'NOME', 'CPF', 'NASCIMENTO', 'MÃE'] 
        list_data = []
        for row in dados:
            list_data.append(
                (
                 row.id,
                 row.nome,
                 row.cpf if row.cpf else '000.000.000-000', # if ternario
                 row.nascimento.strftime("%x"),
                 row.mae   
                )
            )        
       
        self.model = CustomTableModel(list_data, colunas)
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
        self.tblListagem.setColumnWidth(3, 250)
        self.tblListagem.setColumnWidth(3, 200)