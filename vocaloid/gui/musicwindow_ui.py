# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/zihanli/program/498-Vocaloid/vocaloid/gui/musicwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 772, 400))
        self.scrollAreaWidgetContents.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.scrollAreaWidgetContents.setMouseTracking(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.picLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.picLabel.setGeometry(QtCore.QRect(0, 0, 771, 1090))
        self.picLabel.setText("")
        self.picLabel.setObjectName("picLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back5Button = QtWidgets.QPushButton(self.centralWidget)
        self.back5Button.setMinimumSize(QtCore.QSize(340, 160))
        self.back5Button.setStyleSheet("font: 36pt \"Arial\";")
        self.back5Button.setObjectName("back5Button")
        self.horizontalLayout.addWidget(self.back5Button, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.next5Button = QtWidgets.QPushButton(self.centralWidget)
        self.next5Button.setMinimumSize(QtCore.QSize(340, 160))
        self.next5Button.setStyleSheet("font: 36pt \"Arial\";")
        self.next5Button.setObjectName("next5Button")
        self.horizontalLayout.addWidget(self.next5Button, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralWidget)

        Ui_MainWindow.retranslateUi(self, MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocaloid"))
        self.back5Button.setText(_translate("MainWindow", "BACK"))
        self.next5Button.setText(_translate("MainWindow", "NEXT"))

