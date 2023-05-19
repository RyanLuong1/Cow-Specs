#!/usr/bin/env python3
import pyqtgraph as pg
import logging

class graphing:
    def __init__(self):
        self._graph_instance = pg.plot()
        self._graph_instance.showGrid(x=True, y=True)
        self._graph_instance.addLegend()
        self._graph_instance.setLabel("left", "v_values", units="y")
        self._graph_instance.setLabel("bottom", "h_values", units="s")        

    def setTitle(self, title, y_label, x_label = 'Time (in seconds)', x_unit="x", y_unit="y"):
        self._graph_instance.setWindowTitle(title)
        self._graph_instance.setLabel("left", y_label, units=y_unit)
        self._graph_instance.setLabel("bottom", x_label, units=x_unit)

    def def_graph(
        self,
        x_list,
        y_list,
        range_x,
        range_y,
        range_x_min=0,
        range_y_min=0,
        color="g",
        symbolType="x",
        symbolName="x",
    ):
        self._graph_instance.setYRange(range_y_min, range_y)
        self._graph_instance.setXRange(range_x_min, range_x)
        try:
            self._graph_instance.plot(
                x_list, y_list, pen=color, symbol=symbolType, symbolBrush=0.2, name=symbolName
            )
        except:
            logging.ERROR("Graph.py: X and Y values must be passed as an array for plotting")


# if __name__ == '__main__':

# importing system
# import sys

# example
# graph1 = graphing()
# graph1.setTitle('Hello')
# graph1.def_graph(range(1,10), range(1,10), 10, 10)

# Start Qt event loop unless running in interactive mode or using
# if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#    QtGui.QApplication.instance().exec_()
# need someway to access the graph from the main program widget
