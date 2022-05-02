from qt_core import *

from views.pages.compenentes.ui_responsalvelEditor import Ui_Dialog

class ResponsavelDialog(QDialog):
    def __init__(self, tipo, id):
        super().__init__()

        self.IdToEdit = id
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        if tipo == 'New':
            self.ui.txtNome.setText('')
        elif tipo == 'Edit':
            self.preencheForm
            
    
    def preencheForm(self):

        self.ui.txtNome.setText('Elias')