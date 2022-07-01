import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCompleter

test_model_data = [
    ('Led Zeppelin - Stairwy to Heaven',[                           # tree
             ('branch', [               # tree.branch
                         ('leaf',[])]), # tree.branch.leaf
             ('roots',  [])]),          # tree.roots
    ('house',[                          # house
                ('kitchen',[]),         # house.kitchen
                ('bedroom',[])]),       # house.bedroom
    ('obj3',[]),                        # etc..
    ('obj4',[])
]


class CodeCompleter(QCompleter):
    ConcatenationRole = Qt.UserRole + 1
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.create_model(data)

    def splitPath(self, path):
        return path.split('.')

    def pathFromIndex(self, ix):
        return ix.data(CodeCompleter.ConcatenationRole)

    def create_model(self, data):
        def addItems(parent, elements, t=""):
            for text, children in elements:
                item = QStandardItem(text)
                data = t + "." + text if t else text
                item.setData(data, CodeCompleter.ConcatenationRole)
                parent.appendRow(item)
                if children:
                    addItems(item, children, data)
        model = QStandardItemModel(self)
        addItems(model, data)
        self.setModel(model)

class mainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.entry = QLineEdit(self)
        self.completer = CodeCompleter(test_model_data, self)
        self.entry.setCompleter(self.completer)
        layout = QVBoxLayout()
        layout.addWidget(self.entry)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    hwind = mainApp()
    hwind.show()
    sys.exit(app.exec_())