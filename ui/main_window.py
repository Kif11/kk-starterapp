# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/main_window.ui'
#
# Created: Tue Sep  6 11:25:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 370)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_view = QtGui.QTableView(self.centralwidget)
        self.table_view.setAcceptDrops(True)
        self.table_view.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.table_view.setDragEnabled(True)
        self.table_view.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.table_view.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.table_view.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.table_view.setShowGrid(False)
        self.table_view.setGridStyle(QtCore.Qt.NoPen)
        self.table_view.setObjectName("table_view")
        self.table_view.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.table_view)
        self.publish_btn = QtGui.QPushButton(self.centralwidget)
        self.publish_btn.setObjectName("publish_btn")
        self.verticalLayout.addWidget(self.publish_btn)
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.verticalLayout.addWidget(self.cancel_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_btn.setText(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
