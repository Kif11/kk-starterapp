# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/drop_area.ui'
#
# Created: Tue Sep  6 11:25:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_drop_area(object):
    def setupUi(self, drop_area):
        drop_area.setObjectName("drop_area")
        drop_area.resize(669, 479)
        self.verticalLayout = QtGui.QVBoxLayout(drop_area)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(drop_area)
        self.label.setStyleSheet("font: 24pt \"Arial\";")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/drop_icon/drop2_icon.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(drop_area)
        QtCore.QMetaObject.connectSlotsByName(drop_area)

    def retranslateUi(self, drop_area):
        drop_area.setWindowTitle(QtGui.QApplication.translate("drop_area", "Form", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
