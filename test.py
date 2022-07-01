import os
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QShortcut, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, \
    QFileDialog
from PyQt5.QtGui import QKeySequence, QIcon


class Notepad(QWidget):

    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')
        self.opn_btn = QPushButton('Open')
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_open.activated.connect(self.on_open)
        self.shortcut_close = QShortcut(QKeySequence('Ctrl+W'), self)
        self.shortcut_close.activated.connect(self.closeApp)
        self.shortcut_save = QShortcut(QKeySequence('Ctrl+S'), self)
        self.shortcut_save.activated.connect(self.oc_open)

        self.resize(150, 150)

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)
        self.setLayout(v_layout)
        self.setWindowTitle('Text Editor')
        self.setWindowIcon(QIcon('1.png.png'))

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        try:
            with open(filename[0], 'w') as f:
                my_text = self.text.toPlainText()
                f.write(my_text)
        except:
            pass

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        try:
            with open(filename[0], 'r') as f:
                file_text = f.read()
                self.text.setText(file_text)
        except:
            pass

    def clear_text(self):
        self.text.clear()

    def on_open(self):
        self.open_text()

    def oc_open(self):
        self.save_text()

    def closeApp(self):
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    writer = Notepad()
    sys.exit(app.exec_())
