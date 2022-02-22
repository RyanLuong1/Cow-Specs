# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

#from PySide2.QtWidgets import QApplication, QWidget
#from PySide2.QtCore import QFile
#from PySide2.QtUiTools import QUiLoader
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFile
from PyQt5 import uic, QtGui, QtWidgets

class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = uic.loadUi("form.ui", self)
        self.tree_view = self.ui.treeWidget
        items = []
        value = "100"
        item = QtWidgets.QTreeWidgetItem(["Hardware"])
        ext = value.split(".")[-1].upper()
        child = QtWidgets.QTreeWidgetItem(["", ext])
        item.addChild(child)
        items.append(item)
        self.tree_view.insertTopLevelItems(0, items)

#    def load_ui(self):
#        loader = QUiLoader()
#        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
#        ui_file = QFile(path)
#        ui_file.open(QFile.ReadOnly)
#        loader.load(ui_file, self)
#        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
