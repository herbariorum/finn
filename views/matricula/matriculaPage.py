from qt_core import *

from views.matricula.ui_matricula import Ui_Form

class MatriculaPage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
