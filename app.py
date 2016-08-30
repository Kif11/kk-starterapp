import sys
from PySide import QtGui, QtCore
from ui import Ui_MainWindow

class ComboDelegate(QtGui.QStyledItemDelegate):
    """
    A delegate that places a fully functioning QComboBox in every
    cell of the column to which it's applied
    """
    def __init__(self, parent, options):

        QtGui.QStyledItemDelegate.__init__(self, parent)
        self.options = options

    # def paint(self, painter, option, index):
    #     print '[D] Paint'
    def paint(self, painter, option, index):
        if index.column() == 1:
            progress = index.data()

            progressBarOption = QtGui.QStyleOptionProgressBar()
            progressBarOption.rect = option.rect
            progressBarOption.minimum = 0
            progressBarOption.maximum = 100
            progressBarOption.progress = progress
            progressBarOption.text = str(progress) + "%"
            progressBarOption.textVisible = True

            QtGui.QApplication.style().drawControl(QtGui.QStyle.CE_ProgressBar, progressBarOption, painter)
        else:
            QtGui.QStyledItemDelegate.paint(self, painter, option, index)

    def sizeHint(option, index):
        pass

    def createEditor(self, parent, option, index):
        combo = QtGui.QComboBox(parent)
        combo.addItems(self.options)
        self.connect(combo, QtCore.SIGNAL("currentIndexChanged(int)"), self, QtCore.SLOT("currentIndexChanged()"))
        return combo

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.setCurrentIndex(editor.currentIndex())
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.itemText(editor.currentIndex()))

    @QtCore.Slot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

        self.task_col = 2
        self.type_col = 4

        self.dataChanged.connect(self.on_data_changed)

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        """
        Run for each cell and populate its data
        """
        row = index.row()
        col = index.column()

        # print 'Display data role: ', role

        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            #
            # if col == self.type_col:
            #     combo = QtGui.QComboBox()
            #     self.setIndexWidget(index, combo)
            return None

        return self.mylist[index.row()][index.column()]

    def setData(self, index, value, role):
        """
        This method called when user edit the model from a view
        If successuful will emit dataChanged signal
        """
        if value:
            self.mylist[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def on_data_changed(self, index, *args):

        if index.column() == self.task_col:
            self.mylist[index.row()][self.type_col] = 'HEY'



    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

class Model(object):
    def __init__(self):
        self._update_funcs = []

        # variable placeholders
        self.running = False

    # subscribe a view method for updating
    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    # unsubscribe a view method for updating
    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    # update registered view methods
    def announce_update(self):
        for func in self._update_funcs:
            func()

class MainView(QtGui.QMainWindow):

    def __init__(self, model, main_ctrl, parent=None):

        QtGui.QMainWindow.__init__(self, parent)

        self.model = model
        self.main_ctrl = main_ctrl

        self.build_ui()

        # register func with model for future model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

        header = ['File', 'Entity', 'Task', 'Name', 'Type', 'Mov', 'Comment']
        data_list = [
            ['/file/path', 22, 'plate', 'GS', 'ClientDPX', 'x', 'Default'],
            ['/file2/path2', 33, 'lgt', 'FG', 'ClientDPX', 'x', 'Default'],
        ]
        table_model = MyTableModel(self, data_list, header)
        self.ui.table_view.setModel(table_model)


        # self.ui.table_view.setItemDelegateForColumn(4, ComboDelegate(self, ['One', 'Two']))
        self.ui.table_view.setItemDelegate(ComboDelegate(self, ['One', 'Two']))


    # properties to read/write widget value
    @property
    def running(self):
        # return self.ui.action_btn.isChecked()
        return 'Some data!'
    @running.setter
    def running(self, value):
        # self.ui.action_btn.setChecked(value)
        self.ui.search_bar.setText(value)
        self.ui.search_bar2.setText(value)
        comment_item = QtGui.QTableWidgetItem('') # Default value
        self.file_table.setItem(cur_row, COMM_COL, comment_item)

    def build_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect signal to method
        self.ui.action_btn.clicked.connect(self.on_running)

    def on_running(self):
        self.main_ctrl.change_running(self.running)

    def update_ui_from_model(self):
        self.running = self.model.running

class MainController(object):

    def __init__(self, model):
        self.model = model

    # called from view class
    def change_running(self, checked):
        print '[D] Data: ', checked
        # put control logic here
        self.model.running = checked
        self.model.announce_update()

class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())

# class ApplicationDialog(QtGui.QMainWindow):
#
#     def __init__(self, parent=None):
#         QtGui.QMainWindow.__init__(self, parent)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#     @QtCore.Slot(str)
#     def on_search_bar_textChanged(self, value):
#         print '[D] Search bar value: ', value

# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     app_dialog = ApplicationDialog()
#     app_dialog.show()
#     sys.exit(app.exec_())
