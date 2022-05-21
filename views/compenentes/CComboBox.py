from PySide6.QtWidgets import QWidget, QLabel, QComboBox, QVBoxLayout


class CComboBox(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        self.mainLayout = QVBoxLayout(self)   
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        
        self.label = QLabel(self)    
        
        self.combo = QComboBox(self)
        
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.combo)

    def setLabelText(self, text):
        self.label.setText(text)

    def getText(self):
        return self.combo.currentText()

    def setText(self, text):
        self.combo.setCurrentText(text)

    def setItems(self, text = []):        
        self.combo.addItems(text)