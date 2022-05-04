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
        
        retorno = responsavelController.selectAll()  
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

    def localizarItem(self):
        retorno = responsavelController.search(self.txtLocalizar.text())
        self.loadTable(retorno)


    def openEditTable(self):  
        indexes = self.tblListagem.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.about(self, 'Aviso', 'Selecione um item na tabela')
            return
        else:            
            index = self.tblListagem.selectedIndexes()[0]        
            id = int(self.tblListagem.model().data(index)) # pego o valor da primeira coluna, no caso o id
            # chama o dialog de edicao
            dlg = ResponsavelDialog('Edit', id)
            
            ret = dlg.exec()
            if ret == QDialog.Accepted:  
                retorno = responsavelController.selectAll()                
                self.loadTable(retorno)         
            else:
                pass

    
    def openNewItem(self):        
        dlg = ResponsavelDialog('New')
        ret = dlg.exec()
        if ret == QDialog.Accepted:
            retorno = responsavelController.selectAll()                
            self.loadTable(retorno) 
        else:
            pass

    def deleteItem(self):
        indexes = self.tblListagem.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.about(self, 'Aviso', 'Selecione o item a ser apagado')
            return
        else:  
            index = self.tblListagem.selectedIndexes()[0]        
            id = int(self.tblListagem.model().data(index))
            msg = QMessageBox.question(self, 'Apagar Registro', 'Você tem certeza que deseja apagar o registro \n de ID {}'.format(id), QMessageBox.Ok | QMessageBox.Cancel)
            if QMessageBox.Ok:
                ret = responsavelController.delete(id)
                if ret == 1:
                    QMessageBox.about(self, 'Sucesso', 'Registro apagado com sucesso.')
                    retorno = responsavelController.selectAll()                
                    self.loadTable(retorno) 
                else:
                    QMessageBox.warning(self, 'Erro', str(ret), QMessageBox.Ok)
                    return
            else:
                return 

    def imprimeSelecao(self):
        pass

    def imprimeTudo(self):
        pass

    def loadTable(self, dados):
        colunas = ['ID', 'NOME', 'CPF', 'EMAIL', 'CONTATO(S)']     
         
        list_data = []
        for row in dados:
            list_data.append(
                (
                    row.id,
                    row.nome,
                    row.cpf,
                    row.email,
                    row.contatos, # pegar os contatos
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
        
        # self.tblListagem.doubleClicked.connect(self.openEditTable)
    

        self.tblListagem.setColumnWidth(0, 50)
        self.tblListagem.setColumnWidth(1, 300)
        self.tblListagem.setColumnWidth(2, 150)
        self.tblListagem.setColumnWidth(3, 250)
        self.tblListagem.setColumnWidth(3, 200)
    
