# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/main_window.ui'
#
# Created: Mon Aug 29 17:19:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_bar = QtGui.QLineEdit(self.centralwidget)
        self.search_bar.setObjectName("search_bar")
        self.verticalLayout.addWidget(self.search_bar)
        self.table_view = QtGui.QTableView(self.centralwidget)
        self.table_view.setObjectName("table_view")
        self.verticalLayout.addWidget(self.table_view)
        self.action_btn = QtGui.QPushButton(self.centralwidget)
        self.action_btn.setObjectName("action_btn")
        self.verticalLayout.addWidget(self.action_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.action_btn.setText(QtGui.QApplication.translate("MainWindow", "Action!", None, QtGui.QApplication.UnicodeUTF8))

