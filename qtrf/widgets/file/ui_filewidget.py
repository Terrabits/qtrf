# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/filewidget.ui',
# licensing of 'designer/filewidget.ui' applies.
#
# Created: Tue Apr  2 20:02:27 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileWidget(object):
    def setupUi(self, FileWidget):
        FileWidget.setObjectName("FileWidget")
        FileWidget.resize(133, 33)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FileWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filename = QtWidgets.QLineEdit(FileWidget)
        self.filename.setReadOnly(True)
        self.filename.setObjectName("filename")
        self.horizontalLayout.addWidget(self.filename)
        self.open = QtWidgets.QPushButton(FileWidget)
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.clear = QtWidgets.QPushButton(FileWidget)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)

        self.retranslateUi(FileWidget)
        QtCore.QMetaObject.connectSlotsByName(FileWidget)

    def retranslateUi(self, FileWidget):
        self.open.setText(QtWidgets.QApplication.translate("FileWidget", "...", None, -1))
        self.clear.setText(QtWidgets.QApplication.translate("FileWidget", "X", None, -1))

