from qt_core import *

from views.pages.ui_responsavel import Ui_formResponsavel
from modelos.CustomTableModel import CustomTableModel
import controller.ResponsavelController as responsavelController

class ResponsavelPage(QWidget, Ui_formResponsavel):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        colunas = ['ID', 'NOME', 'CPF', 'EMAIL', 'CONTATO(S)']        
        responsavel = responsavelController.selectAll()        
        list_data = []
        for row in responsavel:
            list_data.append(
                (
                    row.id,
                    row.nome,
                    row.cpf,
                    row.email,
                    row.contato,
                )
            )        
        self.model = CustomTableModel(list_data, colunas)
        self.tblListagem.setModel(self.model)
        self.tblListagem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # self.horizontal_header.setStretchLastSection(True)
        self.tblListagem.setColumnWidth(0, 20)
        self.tblListagem.setColumnWidth(1, 500)