from qt_core import *

import qtawesome as qta

from views.pages.ui_responsavel import Ui_formResponsavel
from modelos.CustomTableModel import CustomTableModel
import controller.ResponsavelController as responsavelController

from views.pages.compenentes.formResponsavel import ResponsavelDialog

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


from pathlib import Path
import os
from sys import platform
import time


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
        indexes = self.tblListagem.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.about(self, 'Aviso', 'Selecione o item a ser apagado')
            return
        else:  
            index = self.tblListagem.selectedIndexes()[0]        
            id = int(self.tblListagem.model().data(index))

            row = responsavelController.selectById(id)           
            doc_name = row.nome+'.pdf'
            
            if platform == "linux" or platform == "linux2":                
                path_dir = Path.home() / 'Documentos'
                save_name = os.path.join(path_dir, doc_name)
            elif platform == "win32" or platform == "win64":
                path_dir = Path.home() / 'Documents'
                save_name = os.path.join(path_dir, doc_name)           
            try:             
                pdf_name = SimpleDocTemplate(save_name, title="Relatório", pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
                
                path_atual = os.getcwd() + '/static/img'
                Story = []
                logo = os.path.join(path_atual, 'logotipo.jpeg')
                headstyle = ParagraphStyle(
                    name='titulo',
                    fontName='Helvetica-Bold',
                    fontSize=14,
                    leading=10,
                    alignment=TA_CENTER
                )               
                    
                endereco_estabelecimento = "Rua Dom Pedro I, sn - Augustinópolis - TO CEP 77960-000"
                dados_responsavel = "Informações sobre o Responsável"
                im = Image(logo, 2*inch, 2*inch)
                Story.append(im)

                styles = getSampleStyleSheet()
                styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
                styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
                Story.append(Spacer(1, 12))

                ptext = '{}'.format(endereco_estabelecimento)
                Story.append(Paragraph(ptext, styles['Center']))
                Story.append(Spacer(1, 12))

                ptext = '{}'.format(dados_responsavel)
                Story.append(Paragraph(ptext, style=headstyle))

                Story.append(Spacer(1, 30))
                ptext = '<b>Nome do responsável</b>: {}'.format(row.nome)
                Story.append(Paragraph(ptext, styles['Justify']))
                Story.append(Spacer(1, 12))
                ptext = '<b>CPF</b>: {}'.format(row.cpf)
                Story.append(Paragraph(ptext, styles['Justify']))

                Story.append(Spacer(1, 12))
                ptext = '<b>Email</b>: {}'.format(row.email)
                Story.append(Paragraph(ptext, styles['Justify']))

                Story.append(Spacer(1, 12))
                ptext = '<b>Tipo de Responsavilidade</b>: {}'.format(row.tipo_responsavel)
                Story.append(Paragraph(ptext, styles['Justify']))

                Story.append(Spacer(1, 12))
                ptext = '<b>Profissão do Responsável</b>: {}'.format(row.profissao)
                Story.append(Paragraph(ptext, styles['Justify']))

                Story.append(Spacer(1, 12))
                ptext = '<b>Telefone de Contato</b>: {}'.format(row.contatos)
                Story.append(Paragraph(ptext, styles['Justify']))

                Story.append(Spacer(1, 12))
                ptext = '<b>Endereço</b>: {}'.format(row.endereco)
                Story.append(Paragraph(ptext, styles['Justify']))

                pdf_name.build(Story)
                             

            except Exception as e:
                QMessageBox.warning(self, 'Erro', str(e), QMessageBox.Ok)
                return

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
    
    def convPontToMM(self, value):
        return value/0.352777