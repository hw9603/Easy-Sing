# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/zihanli/program/498-Vocaloid/vocaloid/gui/startwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 950)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 950))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 950))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.chooseButton = QtWidgets.QPushButton(self.centralWidget)
        self.chooseButton.setGeometry(QtCore.QRect(290, 120, 391, 181))
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
        self.label.setGeometry(QtCore.QRect(770, 70, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(930, 70, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setGeometry(QtCore.QRect(930, 540, 391, 181))
        self.nextButton.setStyleSheet("font: 36pt \"Arial\";")
        self.nextButton.setObjectName("nextButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(930, 120, 391, 391))
        self.textEdit.setStyleSheet("font: 24pt \"Arial\";")
        self.textEdit.setObjectName("textEdit")
        self.fileLabel = QtWidgets.QLabel(self.centralWidget)
        self.fileLabel.setGeometry(QtCore.QRect(400, 310, 161, 21))
        self.fileLabel.setStyleSheet("font: 18pt \"Arial\";")
        self.fileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileLabel.setObjectName("fileLabel")
        self.backButton = QtWidgets.QPushButton(self.centralWidget)
        self.backButton.setGeometry(QtCore.QRect(290, 540, 391, 181))
        self.backButton.setStyleSheet("font: 36pt \"Arial\";")
        self.backButton.setObjectName("backButton")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(300, 70, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralWidget)

        Ui_MainWindow.retranslateUi(self, MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocaloid"))
        self.chooseButton.setText(_translate("MainWindow", "Choose\n"
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
        self.label_3.setText(_translate("MainWindow", "Choose lyrics file:"))

