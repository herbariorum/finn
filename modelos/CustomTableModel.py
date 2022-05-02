from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QColor
from datetime import date, datetime
import qtawesome as qta

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
            value = self._items[row][col]
            if isinstance(value, datetime):
                return value.strftime("%d/%m/%Y")
            if isinstance(value, str):
                return '{0}'.format(self._items[row][col])
            return value
        elif role == Qt.TextAlignmentRole:   
            if col == 0 or col == 1:         
                return (Qt.AlignLeft + Qt.AlignVCenter)            
            return (Qt.AlignCenter + Qt.AlignHCenter)
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.DecorationRole:
            value = self._items[row][col]
            if isinstance(value, date):
                return qta.icon('ei.calendar', color='black')
            if col == 0:
                return qta.icon('fa.id-card-o', color='#fa7610')
        return None        

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        