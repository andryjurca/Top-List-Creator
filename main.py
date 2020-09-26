import os
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QScrollArea

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

        while self.M - self.m > 2:
            self.me = int((self.m + self.M) / 2)
            # x = input('e mai buna ca ' + lista[me - 1][1] + '? (Y/N)')
            msg = QMessageBox()
            msg.setWindowTitle('???')
            msg.setText("e mai buna ca " + lista[self.me - 1][1] + "?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.buttonClicked.connect(self.cand_apesi_pe_buton)
            x = msg.exec_()
            if x == QMessageBox.Yes:
                self.M = self.me
                self.me = int((self.m + self.M) / 2)
                print(self.m, self.me, self.M, x)
            elif x == QMessageBox.No:
                self.m = self.me + 1
                self.me = int((self.m + self.M) / 2)
                print(self.m, self.me, self.M, x)
            else:
                print(self.m, self.me, self.M, x)


        msg1 = QMessageBox()
        msg1.setWindowTitle('???')
        msg1.setText("e mai buna ca " + lista[self.me - 1][1] + "?")
        msg1.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg1.buttonClicked.connect(self.cand_apesi_pe_buton1)
        x = msg1.exec_()
        if x == QMessageBox.Yes:
            self.continua = False
            return self.m
        elif x == QMessageBox.No:
            self.continua = False
            return self.M
        else:
            print(self.m, self.me, self.M, x)

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
                filehandle.write('%s. ' % listitem[0])
                filehandle.write('%s\n' % listitem[1])

    # def read_list(self):
    #     with open('list.txt', 'r') as filehandle:
    #         filecontents = filehandle.readlines()
    #         self.thislist.clear()
    #         i = 0
    #         j = 0
    #         a = [1000, 'testudrecu']
    #
    #         for line in filecontents:
    #             line = line[:-1]
    #             if j == 0:
    #                 a[0] = int(line)
    #             j = (j + 1) % 2
    #             if j == 0:
    #                 i += 1
    #                 a[1] = line
    #                 b = a[:]
    #                 self.thislist.append(b)

    def read_list(self):
        with open('list.txt', 'r') as filehandle:
            filecontents = filehandle.readlines()
            self.thislist.clear()
            a = [1000, 'testudrecu']
            for line in filecontents:
                x = line.split(". ", 2)
                a[0] = int(x[0])
                if re.search("(\\r|)\\n$", x[1]):
                    x[1] = re.sub("(\\r|)\\n$", "", x[1])

                a[1]=x[1]
                b = a[:]
                self.thislist.append(b)

    def deschide_fisier(self):
        ROOT_DIR = os.path.dirname(os.path.abspath("top_level_file.txt"))
        os.system('cd ' + ROOT_DIR)
        os.system('list.txt')

    def setupUi(self, MainWindow):
        MainWindow.resize(422, 255)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 120, 28))
        self.pushButton2.setGeometry(QtCore.QRect(150, 10, 120, 28))

        # For displaying confirmation message along with user's info.
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))
        # Keeping the text of label empty initially.
        self.label.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QIcon('web.png'))
        MainWindow.setWindowTitle(_translate("MainWindow", "Top List Creator"))
        self.pushButton.setText(_translate("MainWindow", "Adauga Melodie"))
        self.pushButton2.setText(_translate("MainWindow", "Deschide Fisier"))
        self.pushButton.clicked.connect(self.takeinputs)
        self.pushButton2.clicked.connect(self.deschide_fisier)

    def takeinputs(self):
        xx, done1 = QtWidgets.QInputDialog.getText(self, 'Adauga Melodie', 'introdu o noua inregistrare:')
        if xx and done1 != '':
            self.continua = True
        else:
            self.continua = False
        while self.continua:
            self.read_list()
            print(self.thislist)
            L = len(self.thislist)
            print(L)

            place = self.locul(self.thislist)
            self.sorteaza(self.thislist, place, xx)

            print(self.thislist)
            self.write_list()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
