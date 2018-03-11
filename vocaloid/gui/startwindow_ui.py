# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hewen/Stuffs/Winter2018/EECS 498/EECS-498-Vocaloid/vocaloid/gui/startwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.chooseButton = QtWidgets.QPushButton(self.centralWidget)
        self.chooseButton.setGeometry(QtCore.QRect(70, 160, 181, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooseButton.setFont(font)
        self.chooseButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chooseButton.setAutoFillBackground(False)
        self.chooseButton.setStyleSheet("font: 36pt \"Arial\";")
        self.chooseButton.setObjectName("chooseButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(280, 210, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(360, 30, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setGeometry(QtCore.QRect(630, 450, 121, 61))
        self.nextButton.setStyleSheet("font: 36pt \"Arial\";")
        self.nextButton.setObjectName("nextButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(360, 80, 391, 351))
        self.textEdit.setStyleSheet("font: 24pt \"Arial\";")
        self.textEdit.setObjectName("textEdit")
        self.fileLabel = QtWidgets.QLabel(self.centralWidget)
        self.fileLabel.setGeometry(QtCore.QRect(80, 300, 161, 21))
        self.fileLabel.setStyleSheet("font: 18pt \"Arial\";")
        self.fileLabel.setObjectName("fileLabel")
        self.backButton = QtWidgets.QPushButton(self.centralWidget)
        self.backButton.setGeometry(QtCore.QRect(70, 450, 131, 61))
        self.backButton.setStyleSheet("font: 36pt \"Arial\";")
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        Ui_MainWindow.retranslateUi(self, MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocaloid"))
        self.chooseButton.setText(_translate("MainWindow", "Choose\n"
"Lyrics\n"
"File"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">OR</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Type the lyrics:"))
        self.nextButton.setText(_translate("MainWindow", "NEXT"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.fileLabel.setText(_translate("MainWindow", "<html><head/><body><p>No file chosen.</p></body></html>"))
        self.backButton.setText(_translate("MainWindow", "BACK"))

