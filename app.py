import sys
from PySide import QtGui, QtCore
from ui import Ui_MainWindow

class ApplicationDialog(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @QtCore.Slot(str)
    def on_search_bar_textChanged(self, value):
        print '[D] Search bar value: ', value

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app_dialog = ApplicationDialog()
    app_dialog.show()
    sys.exit(app.exec_())
