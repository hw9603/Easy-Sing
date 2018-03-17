# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hewen/Stuffs/Winter2018/EECS 498/EECS-498-Vocaloid/vocaloid/gui/myapp/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from vocaloid.gui.mainwindow_ui import Ui_MainWindow as ui1 # 1
from vocaloid.gui.startwindow_ui import Ui_MainWindow as ui2 # 2
from vocaloid.gui.melodywindow_ui import Ui_MainWindow as ui3 # 3
from vocaloid.gui.musicwindow_ui import Ui_MainWindow as ui5
from vocaloid.gui.generatewindow_ui import Ui_MainWindow as ui4 # 4

class MainUI(object):
    def setupUi(self, MainWindow):
        ui1.setupUi(self, MainWindow)

    def setupUi2(self, MainWindow):
        ui2.setupUi(self, MainWindow)

    def setupUi3(self, MainWindow):
        ui3.setupUi(self, MainWindow)

    def setupUi4(self, MainWindow):
        ui4.setupUi(self, MainWindow)

    def setupUi5(self, MainWindow):
        ui5.setupUi(self, MainWindow)

