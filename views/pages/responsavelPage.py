from qt_core import *

import qtawesome as qta

from views.pages.ui_responsavel import Ui_formResponsavel
from modelos.CustomTableModel import CustomTableModel
import controller.ResponsavelController as responsavelController

from views.pages.compenentes.formResponsavel import ResponsavelDialog

class ResponsavelPage(QWidget, Ui_formResponsavel):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.loadTable()

        self.txtLocalizar.setClearButtonEnabled(True)
        self.txtLocalizar.addAction(qta.icon('fa.search'), QLineEdit.LeadingPosition)
        self.btnNovo.clicked.connect(self.openNewItem)
        self.btnNovo.setIcon(qta.icon('msc.new-file', color='black'))
        self.btnDelete.clicked.connect(self.deleteItem)
        self.btnDelete.setIcon(qta.icon('mdi.delete', color='black'))
        self.btnSelecao.clicked.connect(self.imprimeSelecao)
        self.btnSelecao.setIcon(qta.icon('fa.print', color='black'))
        self.btnListagem.clicked.connect(self.imprimeTudo)
        self.btnListagem.setIcon(qta.icon('fa.print', color='black'))

    def openEditTable(self):        
        index = self.tblListagem.selectedIndexes()[0]
        id = int(self.tblListagem.model().data(index)) # pego o valor da primeira coluna, no caso o id
        # chama o dialog de edicao
        dlg = ResponsavelDialog('Edit', id)
        ret = dlg.exec()
        if ret == QDialog.Accepted:
            print('Editado')
        else:
            print('Cancelado')

    
    def openNewItem(self):        
        dlg = ResponsavelDialog('New')
        ret = dlg.exec()
        if ret == QDialog.Accepted:
            print('Insere')
        else:
            print('Cancelado')

    def deleteItem(self):
        pass

    def imprimeSelecao(self):
        pass

    def imprimeTudo(self):
        pass

    def loadTable(self):
        colunas = ['ID', 'NOME', 'CPF', 'EMAIL']        
        responsavel = responsavelController.selectAll()        
        list_data = []
        for row in responsavel:
            list_data.append(
                (
                    row.id,
                    row.nome,
                    row.cpf,
                    row.email,
                    # row.contato, # pegar os contatos
                )
            )        
        self.model = CustomTableModel(list_data, colunas)
        self.tblListagem.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblListagem.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tblListagem.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblListagem.setAlternatingRowColors(True)
        self.tblListagem.setModel(self.model)
    #   https://localcoder.org/how-to-retrieve-the-selected-row-of-a-qtableview

        self.tblListagem.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.tblListagem.horizontalHeader().setStretchLastSection(True)
        self.tblListagem.verticalHeader().hide()
        
        self.tblListagem.doubleClicked.connect(self.openEditTable)
    

        self.tblListagem.setColumnWidth(0, 50)
        self.tblListagem.setColumnWidth(1, 300)
        self.tblListagem.setColumnWidth(2, 150)
        self.tblListagem.setColumnWidth(3, 250)
        self.tblListagem.setColumnWidth(3, 200)
        