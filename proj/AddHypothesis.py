# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddHypothesis.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddHypothesis(object):
    def setupUi(self, AddHypothesis):
        AddHypothesis.setObjectName("AddHypothesis")
        AddHypothesis.resize(990, 532)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AddHypothesis)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(AddHypothesis)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 951, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(25)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditHypothesisProbability = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditHypothesisProbability.setObjectName("lineEditHypotesisProbability")
        self.gridLayout.addWidget(self.lineEditHypothesisProbability, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lineEditHypothesisName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditHypothesisName.setObjectName("lineEditHypothesisName")
        self.gridLayout.addWidget(self.lineEditHypothesisName, 1, 0, 1, 1)
        self.buttonSaveHypothesis = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonSaveHypothesis.setMinimumSize(QtCore.QSize(150, 40))
        self.buttonSaveHypothesis.setObjectName("buttonSaveHypothesis")
        self.gridLayout.addWidget(self.buttonSaveHypothesis, 0, 2, 2, 1)
        self.tableEvidenceProbability = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableEvidenceProbability.setMinimumSize(QtCore.QSize(0, 426))
        self.tableEvidenceProbability.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableEvidenceProbability.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableEvidenceProbability.setObjectName("tableEvidenceProbability")
        self.tableEvidenceProbability.setColumnCount(3)
        self.tableEvidenceProbability.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvidenceProbability.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvidenceProbability.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEvidenceProbability.setHorizontalHeaderItem(2, item)
        self.tableEvidenceProbability.horizontalHeader().setVisible(True)
        self.tableEvidenceProbability.horizontalHeader().setCascadingSectionResizes(True)
        self.tableEvidenceProbability.horizontalHeader().setDefaultSectionSize(100)
        self.tableEvidenceProbability.horizontalHeader().setHighlightSections(False)
        self.tableEvidenceProbability.horizontalHeader().setMinimumSectionSize(25)
        self.tableEvidenceProbability.horizontalHeader().setSortIndicatorShown(False)
        self.tableEvidenceProbability.horizontalHeader().setStretchLastSection(False)
        self.tableEvidenceProbability.verticalHeader().setVisible(False)
        self.tableEvidenceProbability.verticalHeader().setCascadingSectionResizes(False)
        self.tableEvidenceProbability.verticalHeader().setSortIndicatorShown(False)
        self.tableEvidenceProbability.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableEvidenceProbability, 2, 0, 1, 3)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(AddHypothesis)
        QtCore.QMetaObject.connectSlotsByName(AddHypothesis)

    def retranslateUi(self, AddHypothesis):
        _translate = QtCore.QCoreApplication.translate
        AddHypothesis.setWindowTitle(_translate("AddHypothesis", "Form"))
        self.groupBox.setTitle(_translate("AddHypothesis", "Гипотеза"))
        self.label.setText(_translate("AddHypothesis", "Название"))
        self.label_2.setText(_translate("AddHypothesis", "Априорная вероятность P"))
        self.buttonSaveHypothesis.setText(_translate("AddHypothesis", "Сохранить"))
        item = self.tableEvidenceProbability.horizontalHeaderItem(0)
        item.setText(_translate("AddHypothesis", "Название"))
        item = self.tableEvidenceProbability.horizontalHeaderItem(1)
        item.setText(_translate("AddHypothesis", "Вероятность выполнения свидетельства \n при верности гипотезы"))
        item = self.tableEvidenceProbability.horizontalHeaderItem(2)
        item.setText(_translate("AddHypothesis", "Вероятность выполнения свидетельства \n при неверности гипотезы"))
        self.tableEvidenceProbability.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)