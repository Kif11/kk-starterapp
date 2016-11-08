import sys
from PySide import QtGui, QtCore
from ui import Ui_MainWindow
from model import TableModel

DATA = [
    ['item1', 'item2', 'item3'],
    ['dog1', 'dog2', 'dog3'],
]


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.table_model = TableModel(DATA)
        self.ui.table_view.setModel(self.table_model)

        self.ui.action_btn.clicked.connect(self.on_action_btn)

    def on_action_btn(self):
        print 'DATA: ', self.table_model.data_list

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app_dialog = MainWindow()

    app_dialog.show()
    sys.exit(app.exec_())
