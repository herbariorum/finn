from qt_core import *

from views.pages.ui_home import Ui_Form

class HomePage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)