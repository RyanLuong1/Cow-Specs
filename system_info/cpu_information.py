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
    return psutil.cpu_count(logical = True)

# Current CPU Frequency
def cpu_freq():
    return psutil.cpu_freq(percpu=True)

def extract_info_from_freq():
    #we need to take out the information from cpu_freq(), it's all garbled up
    cpu_freq_decoded = cpu_freq()
    for index in range(len(cpu_freq_decoded)):
        for j in range(0,3): #0 is current, 1 is min, 2 is max
            print(cpu_freq_decoded[index][j]) #cpu_freq_decoded[index][j], index is core, j is temp type

# Current CPU Untilization (Usage)
def cpu_usage():
    return psutil.cpu_percent(interval = 1, percpu=True)

# CPU Tempature (measured in celsius)
def cpu_temperature():
    return psutil.sensors_temperatures()
