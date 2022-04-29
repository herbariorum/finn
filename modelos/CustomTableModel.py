from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QColor
from datetime import date

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent=None):
        QAbstractTableModel.__init__(self)
        self._items = data
        self._headers = headers

    def update(self, dataIn):
        self._items = dataIn

    def rowCount(self, parent):
        return len(self._items)

    def columnCount(self, parent):
        return len(self._headers)

    
    def headerData(self, section, orientation, role):        
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None
            

    def data(self, index, role=Qt.DisplayRole): 
        row = index.row()
        col = index.column()
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return '{0}'.format(self._items[row][col])
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        return None        

    def flags(self, index):
        return Qt.ItemIsEnabled