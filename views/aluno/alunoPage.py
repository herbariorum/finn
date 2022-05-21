from qt_core import *
import qtawesome as qta
from sys import platform
from pathlib import Path
import webbrowser
import os

from views.aluno.ui_aluno import Ui_Form
import controller.AlunoController as alunoController
import controller.ResponsavelController as responsavelController
from modelos.CustomTableModel import CustomTableModel

from views.aluno.forms.form import Form

from PySide6.QtPrintSupport import QPrinter
from math import floor

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

from views.aluno.reporter.header import getHeaderPage
from views.aluno.reporter.table import getTablePage
from views.aluno.reporter.footer import getFooterPage
from views.aluno.reporter.body import getBodyPage

static_dir = QDir.currentPath() + "/static"

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
        ret = form.exec()
        if ret == QDialog.Accepted:
            retorno = alunoController.selectAll()               
            self.loadTable(retorno) 

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
            

    def deleteItem(self):
        indexes = self.tblListagem.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.about(self, 'Aviso', 'Selecione o item a ser apagado')
            return
        else:  
            index = self.tblListagem.selectedIndexes()[0]        
            id = int(self.tblListagem.model().data(index))
            msg = QMessageBox.question(self, 'Apagar Registro', 'Você tem certeza que deseja apagar o registro \n de ID {}'.format(id), QMessageBox.Ok | QMessageBox.Cancel)
            if msg == QMessageBox.Ok:                
                ret = alunoController.delete(id)
                if ret == 1:
                    QMessageBox.about(self, 'Sucesso', 'Registro apagado com sucesso.')
                    retorno = alunoController.selectAll()                
                    self.loadTable(retorno) 
                else:
                    QMessageBox.warning(self, 'Erro', str(ret), QMessageBox.Ok)
                    return
            else:
                return 

    def imprimeSelecao(self):
        indexes = self.tblListagem.selectionModel().selectedRows()
        if not indexes:
            QMessageBox.about(self, 'Aviso', 'Selecione o item a ser impresso')
            return
        else: 
            index = self.tblListagem.selectedIndexes()[0]        
            id = int(self.tblListagem.model().data(index))
            row = alunoController.selectById(id)
            # gera o relatorio
            diretorio = QDir.homePath()+ "/Print"    
            if not os.path.isdir(diretorio):
                os.mkdir(diretorio)
            datetime = QDateTime.currentDateTime()
            save_name = diretorio + "/" + row.nome +'_date_'+ datetime.toString("dd_MM_yyyy") +".pdf"
            try: 
                table_style = TableStyle([
                    # ('GRID', (0,0), (-1,-1), 1, 'red'),
                    ('LEFTPADDING', (0, 0), (-1, -3), 50),  
                    ('BOTTOMPADDING', (0, 0), (-1,-1), 0),   
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'), 
                    ('ALIGNMENT', (0, 1), (-1,-1), 'CENTER')     
                ])
                pdf = Canvas(save_name, pagesize=A4)
                pdf.setTitle('Relatório')
                width, height = A4 #A4 = (210*mm,297*mm) w e h
                heightList = [
                    height * 10 / 100,
                    height * 87 / 100,
                    height * 3 / 100,
                ]
                # 00 (-1, -3) Header
                # 10 (-1, -2) Body
                # 20 (-1, -1) Footer
                mainTable = Table([
                    [getHeaderPage(width, heightList[0])],
                    [getBodyPage(row)],
                    [getFooterPage(width, heightList[2])],                
                ],
                    colWidths= width,
                    rowHeights= heightList 
                )
                mainTable.setStyle(table_style)
                mainTable.wrapOn(pdf, 0, 0)
                mainTable.drawOn(pdf, 0, 0)
                pdf.showPage()
                pdf.save()
                webbrowser.open(save_name)
            except Exception as e:
                QMessageBox.warning(self, 'Erro', str(e), QMessageBox.Ok)
                return

    def imprimeTudo(self):
        item, ok = QInputDialog.getInt(self, 'Impressão', 'Informe o número da página a ser impressa', 0, False)
        if not ok:
            return            
        num_page = item
        diretorio = QDir.homePath()+ "/Print"   
        if not os.path.isdir(diretorio):
            os.mkdir(diretorio)
        datetime = QDateTime.currentDateTime()
        save_name = diretorio + "/lista_aluno_page_" + str(num_page) +'_date_'+ datetime.toString("dd_MM_yyyy") +".pdf" 
        try: 
            table_style = TableStyle([
                # ('GRID', (0,0), (-1,-1), 1, 'red'),
                ('LEFTPADDING', (0, 0), (-1, -3), 50),  
                ('BOTTOMPADDING', (0, 0), (-1,-1), 0),   
                ('VALIGN', (0, 1), (-1, -1), 'TOP'), 
                ('ALIGNMENT', (0, 1), (-1,-1), 'CENTER')          
            ])
            pdf = Canvas(save_name, pagesize=A4)
            pdf.setTitle('Relatório')
            width, height = A4 #A4 = (210*mm,297*mm) w e h
            heightList = [
                height * 10 / 100,
                height * 87 / 100,
                height * 3 / 100,
            ]
            # 00 (-1, -3) Header
            # 10 (-1, -2) Body
            # 20 (-1, -1) Footer
            mainTable = Table([
                [getHeaderPage(width, heightList[0])],
                [getTablePage(num_page, width-50)],
                [getFooterPage(width, heightList[2])],                
            ],
                colWidths= width,
                rowHeights= heightList 
            )
            mainTable.setStyle(table_style)
            mainTable.wrapOn(pdf, 0, 0)
            mainTable.drawOn(pdf, 0, 0)
            pdf.showPage()
            pdf.save()
            webbrowser.open(save_name)
        except Exception as e:
            QMessageBox.warning(self, 'Erro', str(e), QMessageBox.Ok)
            return

    def exibeItem(self):
        print('imprimindo')
        self.imprimeSelecao()
    
    def buscaPais(self, id):
        row = responsavelController.selectById(id)
        return row.nome

    def loadTable(self, dados):
        colunas = ['ID', 'NOME', 'CPF', 'NASCIMENTO', 'MÃE'] 
        list_data = []
        for row in dados:
            list_data.append(
                (
                row.id,
                row.nome,
                '{}.{}.{}-{}'.format(row.cpf[:3], row.cpf[3:6], row.cpf[6:9], row.cpf[9:]) if row.cpf else '00000000000', # if ternario
                row.nascimento.strftime("%x"),
                self.buscaPais(row.mae)
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

    def buscaPais(self, id):
        row = responsavelController.selectById(id)
        return row.nome