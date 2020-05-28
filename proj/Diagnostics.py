# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Diagnostics.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Diagnostics(object):
    def setupUi(self, Diagnostics):
        Diagnostics.setObjectName("Diagnostics")
        Diagnostics.resize(352, 427)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Diagnostics)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Diagnostics)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textQuestion = QtWidgets.QTextEdit(Diagnostics)
        self.textQuestion.setReadOnly(True)
        self.textQuestion.setObjectName("textQuestion")
        self.verticalLayout_2.addWidget(self.textQuestion)
        self.groupBox = QtWidgets.QGroupBox(Diagnostics)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonYes = QtWidgets.QPushButton(self.groupBox)
        self.buttonYes.setMinimumSize(QtCore.QSize(0, 30))
        self.buttonYes.setObjectName("buttonYes")
        self.verticalLayout.addWidget(self.buttonYes)
        self.buttonAlmostYes = QtWidgets.QPushButton(self.groupBox)
        self.buttonAlmostYes.setMinimumSize(QtCore.QSize(0, 30))
        self.buttonAlmostYes.setObjectName("buttonAlmostYes")
        self.verticalLayout.addWidget(self.buttonAlmostYes)
        self.buttonDontKnow = QtWidgets.QPushButton(self.groupBox)
        self.buttonDontKnow.setMinimumSize(QtCore.QSize(0, 30))
        self.buttonDontKnow.setObjectName("buttonDontKnow")
        self.verticalLayout.addWidget(self.buttonDontKnow)
        self.buttonAlmostNo = QtWidgets.QPushButton(self.groupBox)
        self.buttonAlmostNo.setMinimumSize(QtCore.QSize(0, 30))
        self.buttonAlmostNo.setObjectName("buttonAlmostNo")
        self.verticalLayout.addWidget(self.buttonAlmostNo)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Diagnostics)
        QtCore.QMetaObject.connectSlotsByName(Diagnostics)

    def retranslateUi(self, Diagnostics):
        _translate = QtCore.QCoreApplication.translate
        Diagnostics.setWindowTitle(_translate("Diagnostics", "Form"))
        self.label.setText(_translate("Diagnostics", "Вопрос:"))
        self.textQuestion.setHtml(_translate("Diagnostics", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("Diagnostics", "Варианты ответа"))
        self.buttonYes.setText(_translate("Diagnostics", "Да"))
        self.buttonAlmostYes.setText(_translate("Diagnostics", "Скорее да, чем нет"))
        self.buttonDontKnow.setText(_translate("Diagnostics", "Не знаю"))
        self.buttonAlmostNo.setText(_translate("Diagnostics", "Скорее нет, чем да"))
        self.pushButton_4.setText(_translate("Diagnostics", "Нет"))
