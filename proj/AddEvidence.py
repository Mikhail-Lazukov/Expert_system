# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddEvidence.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEvidence(object):
    def setupUi(self, AddEvidence):
        AddEvidence.setObjectName("AddEvidence")
        AddEvidence.resize(495, 221)
        self.gridLayout = QtWidgets.QGridLayout(AddEvidence)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditEvidenceName = QtWidgets.QLineEdit(AddEvidence)
        self.lineEditEvidenceName.setObjectName("lineEditEvidenceName")
        self.gridLayout.addWidget(self.lineEditEvidenceName, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(AddEvidence)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEditEvidenceQuestion = QtWidgets.QLineEdit(AddEvidence)
        self.lineEditEvidenceQuestion.setObjectName("lineEditEvidenceQuestion")
        self.gridLayout.addWidget(self.lineEditEvidenceQuestion, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddEvidence)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.buttonSaveEvidence = QtWidgets.QPushButton(AddEvidence)
        self.buttonSaveEvidence.setMinimumSize(QtCore.QSize(100, 0))
        self.buttonSaveEvidence.setObjectName("buttonSaveEvidence")
        self.gridLayout.addWidget(self.buttonSaveEvidence, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(AddEvidence)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.retranslateUi(AddEvidence)
        QtCore.QMetaObject.connectSlotsByName(AddEvidence)

    def retranslateUi(self, AddEvidence):
        _translate = QtCore.QCoreApplication.translate
        AddEvidence.setWindowTitle(_translate("AddEvidence", "Form"))
        self.label.setText(_translate("AddEvidence", "Название"))
        self.label_2.setText(_translate("AddEvidence", "Вопрос"))
        self.buttonSaveEvidence.setText(_translate("AddEvidence", "Сохранить"))
        self.label_3.setText(_translate("AddEvidence", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Добавление свидетельства</span></p></body></html>"))
