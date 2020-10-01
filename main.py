import os
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QScrollArea, QShortcut

import sys

open('list.txt', 'a').close()


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_area = QScrollArea()
        self.setWindowIcon(QIcon('web.png'))
        self.thislist = [[0, 'a'], [1, 'b']]
        self.L = 0
        self.m = 1
        self.M = self.L + 1
        self.me = 0
        self.continua = True

    def myFunc(self, e):
        return 100 - e[0]

    def locul(self, lista):
        L = len(lista)
        if L == 0:
            self.continua = False
            return 1
        self.m = 1
        self.M = L + 1
        self.me = int((self.m + self.M) / 2)

        while self.M - self.m > 1:
            self.me = int((self.m + self.M) / 2)
            # x = input('e mai buna ca ' + lista[me - 1][1] + '? (Y/N)')
            msg = QMessageBox()
            msg.setWindowTitle('Classification process')
            msg.setWindowIcon(QtGui.QIcon('web.png'))
            msg.setText("Is " + self.xx + " better than " + lista[self.me - 1][1] + "?")
            #msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setEscapeButton(None)
            better = msg.addButton('Yes', QtWidgets.QMessageBox.ActionRole)
            worse = msg.addButton('No', QtWidgets.QMessageBox.ActionRole)
            msg.setIcon(QMessageBox.Question)
            msg.buttonClicked.connect(self.cand_apesi_pe_buton)
            x = msg.exec_()
            print(x)
            if x == 0:
                self.M = self.me
                self.me = int((self.m + self.M) / 2)
                print(self.m, self.me, self.M)
            elif x == 1:
                self.m = self.me + 1
                self.me = int((self.m + self.M) / 2)
                print(self.m, self.me, self.M)
            else:
                print(self.m, self.me, self.M)

        msg1 = QMessageBox()
        msg1.setWindowIcon(QtGui.QIcon('web.png'))
        msg1.setWindowTitle('Classification process')
        better = msg1.addButton('yes', QtWidgets.QMessageBox.ActionRole)
        worse = msg1.addButton('no', QtWidgets.QMessageBox.ActionRole)
        print(self.m, self.me, self.M)
        if self.m == self.M:
            self.continua = False
            return self.m
        msg1.setText("Is " + self.xx + " better than " + lista[self.me - 1][1] + "?")
        #msg1.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        msg1.setIcon(QMessageBox.Question)

        msg1.buttonClicked.connect(self.cand_apesi_pe_buton1)
        x = msg1.exec_()
        if x == 0:
            self.continua = False
            return self.m
        elif x == 1:
            self.continua = False
            return self.M
        else:
            print(self.m, self.me, self.M)

    def cand_apesi_pe_buton(self):
        pass

    def cand_apesi_pe_buton1(self):
        pass

    def sorteaza(self, lista, loc, xx):
        if len(lista) == 0:
            lista.append([loc, xx])
            return
        for i in range(loc - 1, len(lista)):
            lista[i][0] = int(lista[i][0]) + 1
        lista.append([loc, xx])
        lista.sort(key=self.myFunc, reverse=True)

    def write_list(self):
        with open('list.txt', 'w') as filehandle:
            for listitem in self.thislist:
                # filehandle.write('%s. ' % listitem[0])
                filehandle.write('%s\n' % listitem[1])

    def read_list(self):
        with open('list.txt', 'r') as filehandle:
            filecontents = filehandle.readlines()
            self.thislist.clear()
            a = [1000, 'testudrecu']
            i = 0
            for line in filecontents:
                i += 1
                a[0] = i
                a[1] = line
                if re.search("(\\r|)\\n$", a[1]):
                    a[1] = re.sub("(\\r|)\\n$", "", a[1])
                if a[1] != '':
                    b = a[:]
                    self.thislist.append(b)
                else:
                    pass

    def deschide_fisier(self):
        msgb = QMessageBox()
        msgb.setIcon(QMessageBox.Information)
        msgb.setWindowTitle('Information')
        msgb.setWindowIcon(QtGui.QIcon('web.png'))
        msgb.setText("Don't forget to save a copy of the file!")
        msgb.exec_()

        ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
        os.system('cd ' + ROOT_DIR)
        os.system('list.txt')

    def setupUi(self, MainWindow):
        MainWindow.resize(422, 255)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 120, 28))
        self.pushButton2.setGeometry(QtCore.QRect(150, 10, 120, 28))
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))
        self.label.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QIcon('web.png'))
        MainWindow.setWindowTitle(_translate("MainWindow", "Top List Creator"))
        self.pushButton.setText(_translate("MainWindow", "Add listing"))
        self.pushButton2.setText(_translate("MainWindow", "Export list"))
        self.pushButton.clicked.connect(self.takeinputs)
        self.pushButton2.clicked.connect(self.deschide_fisier)

    def takeinputs(self):
        self.xx, done1 = QtWidgets.QInputDialog.getText(self, 'Add listing', 'Listing name')
        if self.xx and done1 != '':
            self.continua = True
        else:
            self.continua = False
        while self.continua:
            self.read_list()
            print(self.thislist)
            L = len(self.thislist)
            print(L)
            place = self.locul(self.thislist)
            self.sorteaza(self.thislist, place, self.xx)
            print(self.thislist)
            self.write_list()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
