# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/filewidget.ui',
# licensing of 'designer/filewidget.ui' applies.
#
# Created: Mon Apr  1 22:51:43 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileWidget(object):
    def setupUi(self, FileWidget):
        FileWidget.setObjectName("FileWidget")
        FileWidget.resize(133, 33)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FileWidget)
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filename = QtWidgets.QLineEdit(FileWidget)
        self.filename.setReadOnly(True)
        self.filename.setObjectName("filename")
        self.horizontalLayout.addWidget(self.filename)
        self.button = QtWidgets.QPushButton(FileWidget)
        self.button.setObjectName("button")
        self.horizontalLayout.addWidget(self.button)

        self.retranslateUi(FileWidget)
        QtCore.QMetaObject.connectSlotsByName(FileWidget)

    def retranslateUi(self, FileWidget):
        self.button.setText(QtWidgets.QApplication.translate("FileWidget", "...", None, -1))

