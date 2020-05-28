# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonResult = QtWidgets.QPushButton(self.centralwidget)
        self.buttonResult.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.buttonResult.setCheckable(False)
        self.buttonResult.setAutoDefault(False)
        self.buttonResult.setDefault(False)
        self.buttonResult.setFlat(False)
        self.buttonResult.setObjectName("buttonResult")
        self.gridLayout.addWidget(self.buttonResult, 1, 1, 1, 1)
        self.buttonExpertMode = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExpertMode.setStyleSheet("font: 14pt \"Sans Serif\";")
        self.buttonExpertMode.setObjectName("buttonExpertMode")
        self.gridLayout.addWidget(self.buttonExpertMode, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonResult.setText(_translate("MainWindow", "Анализ и результат"))
        self.buttonExpertMode.setText(_translate("MainWindow", "Режим эксперта"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:32pt; font-family:Times\">Экспертная система</span></p></body></html>"))
