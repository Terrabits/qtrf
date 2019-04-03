# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/filewidget.ui',
# licensing of 'designer/filewidget.ui' applies.
#
# Created: Tue Apr  2 21:31:59 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileWidget(object):
    def setupUi(self, FileWidget):
        FileWidget.setObjectName("FileWidget")
        FileWidget.resize(131, 22)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FileWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filename = QtWidgets.QLineEdit(FileWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename.sizePolicy().hasHeightForWidth())
        self.filename.setSizePolicy(sizePolicy)
        self.filename.setReadOnly(True)
        self.filename.setObjectName("filename")
        self.horizontalLayout.addWidget(self.filename)
        self.open = QtWidgets.QPushButton(FileWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open.sizePolicy().hasHeightForWidth())
        self.open.setSizePolicy(sizePolicy)
        self.open.setMinimumSize(QtCore.QSize(60, 0))
        self.open.setMaximumSize(QtCore.QSize(60, 16777215))
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.clear = QtWidgets.QPushButton(FileWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setMinimumSize(QtCore.QSize(60, 0))
        self.clear.setMaximumSize(QtCore.QSize(60, 16777215))
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(FileWidget)
        QtCore.QMetaObject.connectSlotsByName(FileWidget)

    def retranslateUi(self, FileWidget):
        self.open.setText(QtWidgets.QApplication.translate("FileWidget", "...", None, -1))
        self.clear.setText(QtWidgets.QApplication.translate("FileWidget", "X", None, -1))

