#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
# Big Thanks to Ryan, Michael, and Brandon for the idea and for helping me fix some bugs.
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
from multiprocessing import freeze_support # removed Process, since it's unused

GB_TO_BYTE = 1073741824

class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = uic.loadUi("form.ui", self)
        self.tree_view = self.ui.treeWidget
    #        print(core_count0())
    #        self.tree_view.itemAt(0, 0).child(0).setText(1, "Bye")

    #        self.tree_view.topLevelItem(1).child(0).setText(3, str(cpu_temperature().pop()))
    #        self.tree_view.topLevelItem(3).child(2).setText(3, str(gpu_temp().pop()))

    def get_network(self, network_function, local_address, remote_address):
        for socket_connections in network_function:
            local_ip_and_port = ""
            remote_ip_and_port = ""
            for attribute in socket_connections[3]:
                local_ip_and_port += str(attribute) + ":"
            for attribute in socket_connections[4]:
                remote_ip_and_port += str(attribute) +":"
            local_ip_and_port = local_ip_and_port[:-1]
            remote_ip_and_port = remote_ip_and_port[:-1]
            local_address.append(local_ip_and_port)
            remote_address.append(remote_ip_and_port)
    def insert_network_to_UI(self, addresses, row_index, child_index_network, child_index_address):
        for address in addresses:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(1, f'{address}')
            self.tree_view.topLevelItem(row_index).child(child_index_network).child(child_index_address).addChild(child)

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
#        test = network_IPv4()[0]
#        print(test[3].ip)
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
        self.get_network(network_IPv4(), network_laddr_IPv4, network_raddr_IPv4)
        self.get_network(network_IPv6(), network_laddr_IPv6, network_raddr_IPv6)
        self.get_network(network_IPv4_TCP(), network_laddr_IPv4_TCP, network_raddr_IPv4_TCP)
        self.get_network(network_IPv6_TCP(), network_laddr_IPv6_TCP, network_raddr_IPv6_TCP)
        for item in network_items:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(0, f'{item}')
            for attribute in network_attributes:
                sub_children = QtWidgets.QTreeWidgetItem()
                sub_children.setText(0, f'{attribute}')
                child.addChild(sub_children)
            self.tree_view.topLevelItem(3).addChild(child)
#        print(network_IPv6()[0])
        self.insert_network_to_UI(network_laddr_IPv4, 3, 0, 0)
        self.insert_network_to_UI(network_raddr_IPv4, 3, 0, 1)
        self.insert_network_to_UI(network_laddr_IPv6, 3, 1, 0)
        self.insert_network_to_UI(network_raddr_IPv6, 3, 1, 1)
        self.insert_network_to_UI(network_laddr_IPv4_TCP, 3, 2, 0)
        self.insert_network_to_UI(network_raddr_IPv4_TCP, 3, 2, 1)
        self.insert_network_to_UI(network_laddr_IPv6_TCP, 3, 3, 0)
        self.insert_network_to_UI(network_raddr_IPv6_TCP, 3, 3, 1)

        child = QtWidgets.QTreeWidgetItem()
        child.setText(0, f'Temperature')
        self.tree_view.topLevelItem(0).addChild(child)
#        self.tree_view.topLevelItem(1).child(1).setText(1, "Hi")
#        self.tree_view.topLevelItem(1).child(1).setText(2, "Mo")
#        self.tree_view.topLevelItem(1).child(1).setText(3, "Bye")
        

        temperature = QtWidgets.QTreeWidgetItem()
        temperature.setText(0, "Temperature")
        self.tree_view.topLevelItem(1).addChild(temperature)    # "GPU"

        usage = QtWidgets.QTreeWidgetItem()
        usage.setText(0, "Usage")
        self.tree_view.topLevelItem(1).addChild(usage)      # "GPU"

        disks = disk_count()
        hdd_sdd = disk_partition()
        for i in range(disks):
            usage = QtWidgets.QTreeWidgetItem()
            usage.setText(0, hdd_sdd[i])
            self.tree_view.topLevelItem(2).addChild(usage)      # Partition

        usage = QtWidgets.QTreeWidgetItem()
        usage.setText(0, "Usage")
        self.tree_view.topLevelItem(4).addChild(usage)      # "RAM"
#        print(cpu_name())

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
        disks = disk_count()
        cores = returnCores()
        core_min = [0] * cores
        core_max = [0] * cores

        while True:
            corecount = cpu_freq()
            cpu_temp_index = self.tree_view.topLevelItem(0).childCount() - 1
            cpu_temp = cpu_temperature()
            min_cpu_temp = 0
            max_cpu_temp = 0
            current_cpu_temp = cpu_temp[0]
            if self.tree_view.topLevelItem(0).child(cpu_temp_index).text(2):
                min_cpu_temp = self.tree_view.topLevelItem(0).child(cpu_temp_index).text(2)
            else:
                min_cpu_temp = current_cpu_temp
            if self.tree_view.topLevelItem(0).child(cpu_temp_index).text(3):
                max_cpu_temp = self.tree_view.topLevelItem(0).child(cpu_temp_index).text(3)
            else:
                min_cpu_temp = current_cpu_temp
            min_cpu_temp = min(float(min_cpu_temp), float(current_cpu_temp))
            max_cpu_temp = max(float(max_cpu_temp), float(current_cpu_temp))
            self.tree_view.topLevelItem(0).child(cpu_temp_index).setText(1, str(current_cpu_temp))
            self.tree_view.topLevelItem(0).child(cpu_temp_index).setText(2, str(min_cpu_temp))
            self.tree_view.topLevelItem(0).child(cpu_temp_index).setText(3, str(max_cpu_temp))

            #include CPU Frequencies here, CORE 0, CORE 1, Core 2
            cpu_usage = get_load()
            for core in range(cores):
                core_current = cpu_usage[core]
                if(core_current > core_max[core]):
                    core_max[core] = core_current
                if(core_min[core] > core_current):
                    core_min[core] = core_current
                self.tree_view.topLevelItem(0).child(core).setText(1, str(core_current))
                self.tree_view.topLevelItem(0).child(core).setText(2, str(core_min[core]))
                self.tree_view.topLevelItem(0).child(core).setText(3, str(core_max[core]))

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

           
            #hdd = disk_partition()
            #self.tree_view.topLevelItem(2).child(0).setText(1, str(hdd[0]))
            #self.tree_view.topLevelItem(2).child(0).setText(1, str(hdd[1]))
            #self.tree_view.topLevelItem(2).child(0).setText(1, str(hdd[2]))


            if memory_min > memory_usage():
                memory_min = memory_usage()
            if memory_max < memory_usage():
                memory_max = memory_usage()
            self.tree_view.topLevelItem(4).child(0).setText(1, str(memory_usage()))
            self.tree_view.topLevelItem(4).child(0).setText(2, str(memory_min))
            self.tree_view.topLevelItem(4).child(0).setText(3, str(memory_max))

            hdd_sdd = disk_partition()
            for i in range(disks):
                current_disk = psutil.disk_usage(hdd_sdd[i])
                self.tree_view.topLevelItem(2).child(i).setText(3, str(current_disk[0]//GB_TO_BYTE) + " GB") #Total
                self.tree_view.topLevelItem(2).child(i).setText(1, str(current_disk[1]//GB_TO_BYTE) + " GB") #Used
                self.tree_view.topLevelItem(2).child(i).setText(2, "Out Of") #No Minimum

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
    freeze_support()
    app = QApplication([])
    widget = Widget()
    update_values_thread = threading.Thread(
        target=widget.update_values, args=(), daemon=True
    )

    widget.text_display()
    update_values_thread.start()
    widget.show()
    
    sys.exit(app.exec_())
