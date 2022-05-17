from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QFrame, QHBoxLayout, QVBoxLayout


class CLabelEdit(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        self.mainLayout = QVBoxLayout(self)   
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
              
        self.label = QLabel(self)    
        # self.label.objectName("CLabel")   
        
        self.lineEdit = QLineEdit(self)
        # self.lineEdit.objectName("CLineEdit")

        self.lineEdit.setStyleSheet("""
            QLineEdit {
                padding: 1px;
                border-style: 2px solid #474747;
                border-bottom: 2px solid #c0c0c0;
            }  
            QLineEdit:hover {
                border-bottom: 2px solid #00aaaa;
            }   
        """)
        
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.lineEdit)

    def setLabelText(self, text):
        self.label.setText(text)

    def text(self):
        return self.lineEdit.text()

    def setText(self, text):
        self.lineEdit.setText(text)

    