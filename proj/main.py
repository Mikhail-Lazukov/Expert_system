import sys
import sqlite3
from PyQt5 import QtCore, QtWidgets, QtGui
from MainWindow import Ui_MainWindow
from ExpertMode import Ui_ExpertMode
from Diagnostics import Ui_Diagnostics
from AddEvidence import Ui_AddEvidence
from AddHypothesis import Ui_AddHypothesis


conn = sqlite3.connect("database.db")
cur = conn.cursor()
tables = """ PRAGMA foreign_keys = on;
             CREATE TABLE IF NOT EXISTS evidence(
                            NAME TEXT PRIMARY KEY,
                            QUESTION TEXT NOT NULL
                            );
             CREATE TABLE IF NOT EXISTS hypothesis(
                            NAME TEXT PRIMARY KEY,
                            PROBABILITY REAL
                            );
             CREATE TABLE IF NOT EXISTS influence_of_evidence(
                            ID INTEGER PRIMARY KEY,
                            HYPOTHESIS_NAME TEXT NOT NULL,
                            EVIDENCE_NAME TEXT NOT NULL,
                            P_IF_TRUE REAL,
                            P_IF_FALSE REAL,
                            FOREIGN KEY(HYPOTHESIS_NAME) REFERENCES hypothesis(NAME) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY(EVIDENCE_NAME) REFERENCES evidence(NAME) ON DELETE CASCADE ON UPDATE CASCADE          
                            );"""
cur.executescript(tables)
conn.commit()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__()
        self.ExpertMode = None
        self.Diagnostics = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Подключение клика к кнопкам
        self.ui.buttonExpertMode.clicked.connect(self.openExpertMode)
        self.ui.buttonResult.clicked.connect(self.openDiagnostics)

    def openExpertMode(self):
        if not self.ExpertMode:
            self.ExpertMode = ExpertMode(self)
        self.ExpertMode.refresh()
        self.ExpertMode.show()

    def openDiagnostics(self):
        if not self.Diagnostics:
            self.Diagnostics = Diagnostics(self)
        self.Diagnostics.show()


class ExpertMode(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(ExpertMode, self).__init__()
        self.signal.connect(self.refresh)
        self.AddEvidence = None
        self.AddHypothesis = None
        self.ui = Ui_ExpertMode()
        self.ui.setupUi(self)
        self.ui.buttonAddEvidence.clicked.connect(self.openAddEvidence)
        self.ui.buttonAddHypothesis.clicked.connect(self.openAddHypothesis)
        self.ui.buttonDeleteEvidence.clicked.connect(self.deleteEvidence)

    def openAddEvidence(self):
        if not self.AddEvidence:
            self.AddEvidence = AddEvidence(self)
        self.signal.emit()
        self.AddEvidence.show()

    def deleteEvidence(self):
        row = self.ui.tableEvidence.currentRow()
        text = self.ui.tableEvidence.item(row, 0).text()
        cur.execute("delete from evidence where NAME='" + "{0}'".format(text))
        conn.commit()
        self.signal.emit()
        print(text)

    def openAddHypothesis(self):
        if not self.AddHypothesis:
            self.AddHypothesis = AddHypothesis(self)
        self.AddHypothesis.show()

    def refresh(self):
        cur.execute("SELECT * from evidence")
        rows = cur.fetchall()
        self.ui.tableEvidence.clear()
        self.ui.tableEvidence.setRowCount(len(rows))
        self.ui.tableEvidence.setHorizontalHeaderLabels(['Название', 'Вопрос'])

        i = 0
        for row in rows:
            j = 0
            for item in row:
                self.ui.tableEvidence.setItem(i, j, QtWidgets.QTableWidgetItem(item))
                j += 1
            i += 1


class AddEvidence(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddEvidence, self).__init__()
        self.ui = Ui_AddEvidence()
        self.ui.setupUi(self)
        self.ui.buttonSaveEvidence.clicked.connect(self.saveEvidence)

    def saveEvidence(self):
        name = self.ui.lineEditEvidenceName.text()
        question = self.ui.lineEditEvidenceQuestion.text()
        cur.execute("insert into evidence (NAME, QUESTION) values ('{0}','{1}')".format(name, question))
        conn.commit()
        self.ui.lineEditEvidenceName.clear()
        self.ui.lineEditEvidenceQuestion.clear()
        self.close()


class AddHypothesis(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddHypothesis, self).__init__()
        self.ui = Ui_AddHypothesis()
        self.ui.setupUi(self)
        self.ui.buttonSaveHypothesis.clicked.connect(self.saveHypothesis)

    def saveHypothesis(self):
        name = self.ui.lineEditHypothesisName.text()
        probability = float(self.ui.lineEditHypothesisProbability.text())
        cur.execute("insert into hypothesis (NAME, PROBABILITY) values ('{0}','{1}')".format(name, probability))
        conn.commit()
        self.ui.lineEditHypothesisName.clear()
        self.ui.lineEditHypothesisProbability.clear()
        self.close()


class Diagnostics(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Diagnostics, self).__init__()
        self.ui = Ui_Diagnostics()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWin()
    application.show()

    sys.exit(app.exec_())