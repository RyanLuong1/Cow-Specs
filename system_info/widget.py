#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
from operator import truediv
import os
from pathlib import Path
import sys
import threading
import time
from cpu_information import *
from gpu_information import *
from system_information import *
import gpu_information
import importlib
from importlib import reload

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
        """Fixed Categories displayed"""
#        motherboard_items = ["Voltages", "Temperatures", "Fans", "Controls"]
        CPU_items = ["Clocks", "Temperatures", "Powers", "Memory"]
        RAM_items = ["Load", "Data"]
        GPU_items = [
            "Clocks",
            "Temperatures",
            "Load",
            "Fans",
            "Controls",
            "Powers",
            "Data",
        ]
#        print(network_IPv4())
        test = network_IPv4()[0]
        print(test[3].ip)
        network_items = ["IPv4", "IPv6", "TCP over IPv4", "TCP over IPv6"]
        network_attributes = ["Local address", "Remote address"]
        network_laddr_IPv4 = []
        network_raddr_IPv4 = []
        network_laddr_IPv6 = []
        network_raddr_IPv6 = []
        network_laddr_IPv4_TCP = []
        network_raddr_IPv4_TCP = []
        network_laddr_IPv6_TCP = []
        network_raddr_IPv6_TCP = []
        hardwares = [cpu_name(), gpu_name(), "Storage", "Network", "RAM"]
        for hardware in hardwares[::-1]:
            parent = QtWidgets.QTreeWidgetItem([hardware])
            self.tree_view.insertTopLevelItem(0, parent)
        for core in core_count0():
            child = QtWidgets.QTreeWidgetItem()
            child.setText(0, f'Core #{core}')
            self.tree_view.topLevelItem(0).addChild(child)
        for socket_connections in network_IPv4():
            local_ip_and_port = ""
            remote_ip_and_port = ""
            for attribute in socket_connections[3]:
                local_ip_and_port += str(attribute) + ":"
            for attribute in socket_connections[4]:
                remote_ip_and_port += str(attribute) + ":"
            local_ip_and_port = local_ip_and_port[:-1]
            remote_ip_and_port = remote_ip_and_port[:-1]
            network_laddr_IPv4.append(local_ip_and_port)
            network_raddr_IPv4.append(remote_ip_and_port)
        for socket_connections in network_IPv6():
            local_ip_and_port = ""
            remote_ip_and_port = ""
            for attribute in socket_connections[3]:
                local_ip_and_port += str(attribute) + ":"
            for attribute in socket_connections[4]:
                remote_ip_and_port += str(attribute) + ":"
            local_ip_and_port = local_ip_and_port[:-1]
            remote_ip_and_port = remote_ip_and_port[:-1]
            network_laddr_IPv6.append(local_ip_and_port)
            network_raddr_IPv6.append(remote_ip_and_port)
        for socket_connections in network_IPv4_TCP():
            local_ip_and_port = ""
            remote_ip_and_port = ""
            for attribute in socket_connections[3]:
                local_ip_and_port += str(attribute) + ":"
            for attribute in socket_connections[4]:
                remote_ip_and_port += str(attribute) + ":"
            local_ip_and_port = local_ip_and_port[:-1]
            remote_ip_and_port = remote_ip_and_port[:-1]
            network_laddr_IPv4_TCP.append(local_ip_and_port)
            network_raddr_IPv4_TCP.append(remote_ip_and_port)
        for socket_connections in network_IPv6_TCP():
            local_ip_and_port = ""
            remote_ip_and_port = ""
            for attribute in socket_connections[3]:
                local_ip_and_port += str(attribute) + ":"
            for attribute in socket_connections[4]:
                remote_ip_and_port += str(attribute) + ":"
            local_ip_and_port = local_ip_and_port[:-1]
            remote_ip_and_port = remote_ip_and_port[:-1]
            network_laddr_IPv6_TCP.append(local_ip_and_port)
            network_raddr_IPv6_TCP.append(remote_ip_and_port)
        for item in network_items:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(0, f'{item}')
            for attribute in network_attributes:
                sub_children = QtWidgets.QTreeWidgetItem()
                sub_children.setText(0, f'{attribute}')
                child.addChild(sub_children)
            self.tree_view.topLevelItem(3).addChild(child)
        print(network_IPv6()[0])
        for address in network_laddr_IPv4:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(0).child(0).addChild(child)
        for address in network_raddr_IPv4:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(0).child(1).addChild(child)
        for address in network_laddr_IPv6:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(1).child(0).addChild(child)
        for address in network_raddr_IPv6:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(1).child(1).addChild(child)
        for address in network_laddr_IPv4_TCP:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(2).child(0).addChild(child)
        for address in network_raddr_IPv4_TCP:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(2).child(1).addChild(child)
        for address in network_laddr_IPv6_TCP:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(3).child(0).addChild(child)
        for address in network_raddr_IPv6_TCP:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(3).child(3).child(1).addChild(child)

        child = QtWidgets.QTreeWidgetItem()
        child.setText(0, f'Temperature')
        self.tree_view.topLevelItem(0).addChild(child)
#        self.tree_view.topLevelItem(1).child(1).setText(1, "Hi")
#        self.tree_view.topLevelItem(1).child(1).setText(2, "Mo")
#        self.tree_view.topLevelItem(1).child(1).setText(3, "Bye")
        self.tree_view.topLevelItem(0).child(0).setText(1, str(core_count0()[0]))

        temperature = QtWidgets.QTreeWidgetItem()
        temperature.setText(0, "Temperature")
        self.tree_view.topLevelItem(1).addChild(temperature)    # "GPU"

        usage = QtWidgets.QTreeWidgetItem()
        usage.setText(0, "Usage")
        self.tree_view.topLevelItem(1).addChild(usage)      # "GPU"

        usage = QtWidgets.QTreeWidgetItem()
        usage.setText(0, "Usage")
        self.tree_view.topLevelItem(4).addChild(usage)      # "RAM"
        print(cpu_name())

    def update_values(self):
        """Update values constantly to display up to date information, store max and min for each category."""
        #Initialize all necessary variables here before the loop
        # print(cpu_temperature())
        gpu_min = gpu_usage()
        gpu_max = 0
        gpu_temp_min = gpu_temp()
        gpu_temp_max = 0
        memory_min = memory_usage()
        memory_max = 0

        while True:
            corecount = cpu_freq()
            cpu_temp = cpu_temperature()
            print(len(corecount))
            for index in range(len(corecount)):
                for j in range(1,4):
                    self.tree_view.topLevelItem(0).child(index).setText(j, str(corecount[index][j-1]))
            cpu_children = self.tree_view.topLevelItem(0).childCount()
            self.tree_view.topLevelItem(0).child(cpu_children - 1).setText(1, str(cpu_temp['k10temp'][0][1]))
            print(cpu_children)

            importlib.reload(gpu_information)
            if gpu_temp_min > gpu_temp():
                gpu_temp_min = gpu_temp()
            if gpu_temp_max < gpu_temp():
                gpu_temp_max = gpu_temp()
            self.tree_view.topLevelItem(1).child(0).setText(1, str(gpu_temp()))
            self.tree_view.topLevelItem(1).child(0).setText(2, str(gpu_temp_min))
            self.tree_view.topLevelItem(1).child(0).setText(3, str(gpu_temp_max))

            if gpu_min > gpu_usage():
                gpu_min = gpu_usage()
            if gpu_max < gpu_usage():
                gpu_max = gpu_usage()
            self.tree_view.topLevelItem(1).child(1).setText(1, str(gpu_usage()))
            self.tree_view.topLevelItem(1).child(1).setText(2, str(gpu_min))
            self.tree_view.topLevelItem(1).child(1).setText(3, str(gpu_max))

            if memory_min > memory_usage():
                memory_min = memory_usage()
            if memory_max < memory_usage():
                memory_max = memory_usage()
            self.tree_view.topLevelItem(4).child(0).setText(1, str(memory_usage()))
            self.tree_view.topLevelItem(4).child(0).setText(2, str(memory_min))
            self.tree_view.topLevelItem(4).child(0).setText(3, str(memory_max))
            # add more values to print out from here

            time.sleep(1)

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
    update_values_thread = threading.Thread(
        target=widget.update_values, args=(), daemon=True
    )

    widget.text_display()
    update_values_thread.start()
    widget.show()
    
    sys.exit(app.exec_())
