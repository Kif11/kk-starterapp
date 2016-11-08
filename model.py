from PySide import QtGui, QtCore


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data, header=[], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.data_list = data
        self.header = header

    def rowCount(self, parent):
        if not self.data_list:
            return 0
        return len(self.data_list)

    def columnCount(self, parent):
        if not self.data_list:
            return 0
        return len(self.data_list[0])

    def headerData(self, col, orientation, role):
        if not self.header:
            return None
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        flags = (
            QtCore.Qt.ItemIsEditable |
            QtCore.Qt.ItemIsEnabled |
            QtCore.Qt.ItemIsSelectable
        )
        return flags

    def data(self, index, role):
        if not index.isValid():
            return None

        value = self.data_list[index.row()][index.column()]

        if role == QtCore.Qt.DisplayRole:
            return value

        elif role == QtCore.Qt.EditRole:
            return index.data()

    def setData(self, index, value, role):
        """
        This method called when user edit the model from a view
        If successful will emit dataChanged signal
        """
        if role == QtCore.Qt.EditRole:
            self.data_list[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)

            return True
        else:
            return False
