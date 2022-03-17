import platform
import psutil
import logging
try:
    import wmi #import WMI if utilizing windows
    found_wmi = True
except ImportError:
    logging.warn('cpu_information.py: WMI is not found: Ignore if using Linux')
    found_wmi = False

# CPU physical cores
def core_count0():
    cpu_count = psutil.cpu_count(logical = False)
    cpu_list = [i for i in range(cpu_count)]
    return cpu_list

# CPU Logical cores (for Hyperthreading)
def core_count1():
    return {psutil.cpu_count(logical = True)}

# Current CPU Frequency
def cpu_freq():
    return {psutil.cpu_freq().current}

# Minimum CPU Frequency
def cpu_freq_min():
    return {psutil.cpu_freq().min}

# Maximum CPU Frequency
def cpu_fre_max():
    return {psutil.cpu_freq().max}

# Current CPU Untilization (Usage)
def cpu_usage():
    return {psutil.cpu_percent(interval = 1)}

# CPU Tempature (measured in celsius)
def cpu_temperature():
    if (found_wmi): #use WMI by default
        w = wmi.WMI(namespace ="root\OpenHardwareMonitor")
        for sensor in w.Sensor():
            if sensor.SensorType ==u'Temperature':
                print(sensor.value)
                return sensor.Value
#    return psutil.sensors_temperatures()
