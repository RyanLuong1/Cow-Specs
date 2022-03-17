import QtQuick 2.15
import QtQuick.Controls 2.15

class Sensor:
    def _init_(name, max_value, min_value, current_value):
    self.name = name
    self.max_value = max_value
    self.min_value = min_value
    self.current_value = current_value
