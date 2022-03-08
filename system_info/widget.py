#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
from operator import truediv
import os
from pathlib import Path
import sys
import threading
from cpu_information import *
from gpu_information import *
from system_information import *

# from PySide2.QtWidgets import QApplication, QWidget
# from PySide2.QtCore import QFile
# from PySide2.QtUiTools import QUiLoader
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFile
from PyQt5 import uic, QtGui, QtWidgets


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = uic.loadUi("form.ui", self)
        self.tree_view = self.ui.treeWidget

    #        print(core_count0())
    #        self.tree_view.itemAt(0, 0).child(0).setText(1, "Bye")

    #        self.tree_view.topLevelItem(1).child(0).setText(3, str(cpu_temperature().pop()))
    #        self.tree_view.topLevelItem(3).child(2).setText(3, str(gpu_temp().pop()))

    def text_display(self):
        self.tree_view.topLevelItem(1).child(0).setText(1, str(cpu_freq().pop()))
        self.tree_view.topLevelItem(1).child(0).setText(2, str(cpu_freq_min().pop()))
        self.tree_view.topLevelItem(1).child(0).setText(3, str(cpu_fre_max().pop()))

    def core_program(self):
        self.text_display()


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
    threadOne = threading.Thread(target=widget.text_display, args=(), daemon=True)
    threadOne.start()
    widget.show()
    threadOne.join()
    sys.exit(app.exec_())
