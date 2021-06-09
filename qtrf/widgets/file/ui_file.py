# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FileWidget:
    def setupUi(self, FileWidget):
        if not FileWidget.objectName():
            FileWidget.setObjectName(u"FileWidget")
        self.horizontalLayout = QHBoxLayout(FileWidget)
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.filename = QLineEdit(FileWidget)
        self.filename.setObjectName(u"filename")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename.sizePolicy().hasHeightForWidth())
        self.filename.setSizePolicy(sizePolicy)
        self.filename.setFocusPolicy(Qt.NoFocus)
        self.filename.setReadOnly(True)

        self.horizontalLayout.addWidget(self.filename)

        self.open = QPushButton(FileWidget)
        self.open.setObjectName(u"open")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open.sizePolicy().hasHeightForWidth())
        self.open.setSizePolicy(sizePolicy1)
        self.open.setMinimumSize(QSize(60, 0))
        self.open.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.open)

        self.clear = QPushButton(FileWidget)
        self.clear.setObjectName(u"clear")
        sizePolicy1.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy1)
        self.clear.setMinimumSize(QSize(60, 0))
        self.clear.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.clear)

        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(FileWidget)

        QMetaObject.connectSlotsByName(FileWidget)
    # setupUi

    def retranslateUi(self, FileWidget):
        self.open.setText(QCoreApplication.translate("FileWidget", u"...", None))
        self.clear.setText(QCoreApplication.translate("FileWidget", u"X", None))
        pass
    # retranslateUi

