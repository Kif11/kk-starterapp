import sys
from PySide import QtGui, QtCore
from ui import Ui_MainWindow, Ui_drop_area

# sg_tasks = sg.find('Task', [], ['entity', 'content'])
sg_tasks = [
 {'content': 'mp',
  'entity': {'id': 1404, 'name': 'Test_asset', 'type': 'Asset'},
  'id': 6704,
  'type': 'Task'},
 {'content': 'plate',
  'entity': {'id': 1244, 'name': 'lpk0000', 'type': 'Shot'},
  'id': 6522,
  'type': 'Task'},
]

taks_types = {}
for t in sg_tasks:
    taks_types[t['entity']['name'], t['content']] = t['entity']

# import pdb; pdb.set_trace()

header = ['Status', 'File', 'Entity', 'Task', 'Name', 'Version', 'Type', 'Mov', 'Comment']

data_list = [
    [0, '/file/path/whicis/pretty/long/may/be/evenlonger/then/this/it/is/still/notlogenoght', 'lpk0000', 'plate', 'GS', 1, [0, []], True, 'Default'],
    [1, '/file2/path2', 'Test_asset', 'lgt', 'FG', 12, [0, ['AssetDPX', 'AssetEXR']], False, 'Default'],
]

TABLE_EVEN_ROW_COLOR = QtGui.QColor(245, 245, 245)

class DropOverlay(QtGui.QLabel):

    def __init__(self, parent=None):
        super(DropOverlay, self).__init__(parent)

        self.ui = Ui_drop_area()
        self.ui.setupUi(self)
        self.lbl = self.ui.label

        self.lbl.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lbl.parent = parent
        palette = QtGui.QPalette(self.lbl.palette())
        palette.setColor(palette.Background, QtCore.Qt.transparent)

    def showEvent(self, even):

        parent_geo = self.lbl.parent.frameGeometry()
        lable_geo = self.lbl.geometry()

        # Find center point of the parent widget and move our label there
        parent_center = QtCore.QPoint(
            (parent_geo.width() / 2) - (lable_geo.width() / 2),
            (parent_geo.height() / 2) - (lable_geo.height() / 1.75)
        )
        self.move(parent_center)

class StatusDelegate(QtGui.QStyledItemDelegate):
    """
    Define display style of status cell
    """
    def __init__(self, parent):
        QtGui.QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        """
        Important, otherwise an editor is created if the user clicks in this cell.
        ** Need to hook up a signal to the model
        """
        return None

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.
        """
        if index.data() == 0:
            pic = QtGui.QPixmap(':/status/status_wts.png')
        elif index.data() == 1:
            pic = QtGui.QPixmap(':/status/status_ok.png')
        elif index.data() == 2:
            pic = QtGui.QPixmap(':/status/status_warning.png')
        elif index.data() == 3:
            pic = QtGui.QPixmap(':/status/status_error.png')

        painter.drawPixmap(option.rect.topLeft(), pic.scaled(option.rect.width(), option.rect.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def editorEvent(self, event, model, option, index):
        return False

class CheckBoxDelegate(QtGui.QStyledItemDelegate):
    """
    A delegate that places a fully functioning QCheckBox in every
    cell of the column to which it's applied
    """
    def __init__(self, parent):
        QtGui.QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        """
        Important, otherwise an editor is created if the user clicks in this cell.
        ** Need to hook up a signal to the model
        """
        return None

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.
        """
        checked = index.model().data(index, QtCore.Qt.DisplayRole)

        opt = QtGui.QStyleOptionButton()

        if (index.flags() & QtCore.Qt.ItemIsEditable) > 0:
            opt.state |= QtGui.QStyle.State_Enabled
        else:
            opt.state |= QtGui.QStyle.State_ReadOnly

        if checked:
            opt.state |= QtGui.QStyle.State_On
        else:
            opt.state |= QtGui.QStyle.State_Off

        opt.rect = self.getCheckBoxRect(option)

        opt.state |= QtGui.QStyle.State_Enabled

        if index.row() % 2 == 0:
            painter.fillRect(option.rect, TABLE_EVEN_ROW_COLOR)

        QtGui.QApplication.style().drawControl(QtGui.QStyle.CE_CheckBox, opt, painter)

    def editorEvent(self, event, model, option, index):
        """
        Change the data in the model and the state of the checkbox
        """
        if not (index.flags() & QtCore.Qt.ItemIsEditable) > 0:
            return False

        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            # Change the checkbox-state
            self.setModelData(None, model, index)

        return True

    def setModelData (self, editor, model, index):
        """
        The user wanted to change the old state in the opposite.
        """
        new_value = not index.model().data(index, QtCore.Qt.DisplayRole)
        model.setData(index, new_value, QtCore.Qt.EditRole)

    def getCheckBoxRect(self, option):
        check_box_style_option = QtGui.QStyleOptionButton()
        check_box_rect = QtGui.QApplication.style().subElementRect(
            QtGui.QStyle.SE_CheckBoxIndicator, check_box_style_option, None
        )
        check_box_point = QtCore.QPoint (
            option.rect.x() +
            option.rect.width() / 2 -
            check_box_rect.width() / 2,
            option.rect.y() +
            option.rect.height() / 2 -
            check_box_rect.height() / 2
        )
        return QtCore.QRect(check_box_point, check_box_rect.size())

class ComboBoxDelegate(QtGui.QStyledItemDelegate):
    """
    A delegate that places a fully functioning QComboBox in every
    cell of the column to which it's applied
    """
    def __init__(self, parent):
        QtGui.QStyledItemDelegate.__init__(self, parent)

    def displayText(self, value, locale=None):

        cur_index = value[0]
        options = value[1]

        if options:
            display_value = options[cur_index]
        else:
            display_value = 'None'

        return display_value

    # def paint(self, painter, option, index):
    #     """
    #     Responsible for defining our widget appearance
    #     """
    #
    #     opt = QtGui.QStyleOptionComboBox()
    #     opt.rect = option.rect
    #
    #     style = QtGui.QApplication.style()
    #     style.drawComplexControl(QtGui.QStyle.CC_ComboBox, opt, painter)
    #
    #     # Call parent class
    #     # Otherwise the combo box wont display out item
    #     QtGui.QStyledItemDelegate.paint(self, painter, option, index)

    def createEditor(self, parent, option, index):

        if not index.isValid():
            return False

        list_items = index.data()[1]

        comboBox = QtGui.QComboBox(parent)
        comboBox.insertItems(0, list_items)

        return comboBox

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.setCurrentIndex(index.data()[0])
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        new_data = [editor.currentIndex(), index.data()[1]]
        model.setData(index, new_data, QtCore.Qt.EditRole)

    @QtCore.Slot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

class IngestTableModel(QtCore.QAbstractTableModel):

    def __init__(self, parent, mylist, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

        self.enti_col = header.index('Entity')
        self.task_col = header.index('Task')
        self.type_col = header.index('Type')
        self.move_col = header.index('Mov')

        self.dataChanged.connect(self.on_data_changed)

    def rowCount(self, parent):
        if not self.mylist:
            return 0

        return len(self.mylist)

    def columnCount(self, parent):
        if not self.mylist:
            return 0

        return len(self.mylist[0])

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled # | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):

        if not index.isValid():
            return None

        if role == QtCore.Qt.DisplayRole:
            value = self.mylist[index.row()][index.column()]

            if index.column() == self.type_col:
                value = self._set_publish_types(index)

            return value

        elif role == QtCore.Qt.EditRole:
            return index.data()

        elif role == QtCore.Qt.BackgroundColorRole:
            value = self.mylist[index.row()][index.column()]

            if index.row() % 2 == 0:
                return TABLE_EVEN_ROW_COLOR

            if value == '':
                return QtGui.QColor(240, 220, 240)

        else:
            return None

    def setData(self, index, value, role):
        """
        This method called when user edit the model from a view
        If successuful will emit dataChanged signal
        """

        if role == QtCore.Qt.EditRole:
            self.mylist[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)

            return True
        else:
            return False

    def on_data_changed(self, index, *args):
        # If user changed the context of current publish
        if index.column() == self.task_col or index.column() == self.enti_col:
            self._set_publish_types(index)

    def get_sg_entity_id(self, entiry_name, task_name):
        entity = taks_types.get((entiry_name, task_name))
        entity_id = entity.get('id')
        return entity_id

    def _get_publish_types(self, entiry_name, task_name):
        entity = taks_types.get((entiry_name, task_name), {})
        entity_type = entity.get('type')

        if entity_type == 'Shot':
            publish_type_list = ['ShotSmth', 'lpkHey']
        elif entity_type == 'Asset':
            publish_type_list = ['AssetSmth', 'Test_asset111']
        else:
            publish_type_list = []

        return publish_type_list

    def _set_publish_types(self, index):

        cur_row = self.mylist[index.row()]

        if cur_row[self.type_col]:
            selected_index = cur_row[self.type_col][0]
        else:
            selected_index = 0

        entiry_name = cur_row[self.enti_col]
        task_name = cur_row[self.task_col]

        publish_types = self._get_publish_types(entiry_name, task_name)

        cur_row[self.type_col] = [selected_index, publish_types]

        return cur_row[self.type_col]

class IngestMainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):

        # QtGui.QMainWindow.__init__(self, parent)

        # For dev
        QtGui.QMainWindow.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.table_model = IngestTableModel(self, data_list, header)
        self.ui.table_view.setModel(self.table_model)

        self.ui.table_view.setItemDelegateForColumn(header.index('Status'), StatusDelegate(self))
        self.ui.table_view.setItemDelegateForColumn(header.index('Type'), ComboBoxDelegate(self))
        self.ui.table_view.setItemDelegateForColumn(header.index('Mov'), CheckBoxDelegate(self))

        self.ui.table_view.dragEnterEvent = self.table_view_dragEnterEvent
        self.ui.table_view.dragLeaveEvent = self.table_view_dragLeaveEvent
        self.ui.table_view.dragMoveEvent = self.table_view_dragMoveEvent
        self.ui.table_view.dropEvent = self.table_view_dropEvent

        self.resize_table_view()

        # Connect buttons signals
        self.ui.publish_btn.clicked.connect(self.on_publish)

        self.drop_overlay = DropOverlay(self.ui.table_view)
        self.drop_overlay.hide()

    def table_view_dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def table_view_dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            self.drop_overlay.show()
            event.accept()
        else:
            event.ignore()

    def table_view_dragLeaveEvent(self, event):
        self.drop_overlay.hide()
        event.accept()

    def table_view_dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            self.drop_overlay.hide()

            droped_files = event.mimeData().urls()

            self.add_publish_items(droped_files)
        else:
            event.ignore()

    def resize_table_view(self):
        self.ui.table_view.resizeColumnsToContents()
        self.ui.table_view.setColumnWidth(header.index('File'), 200)
        self.ui.table_view.setColumnWidth(header.index('Type'), 100)

    def add_publish_items(self, files):
        """
        param files: List of QtCore.QUrl's
        """
        for f in files:
            new_pub_item = [0, f.path(), 'sub1111', 'match', 'GS', 22, [1, [['DPX', 'EXR']]], True, 'o', 'Default']
            data_list.append(new_pub_item)

        self.table_model.reset()
        self.resize_table_view()

    def on_publish(self):
        print '[D] Publish btn pressed! '
        for p in data_list:
            p[0] = 1
            self.table_model.reset()

class App(QtGui.QApplication):

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_view = IngestMainWindow()
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
