import platform
import psutil
import logging
import cpuinfo
import random

try:
    import wmi #import WMI if utilizing windows
    found_wmi = True
except ImportError:
    logging.warn('cpu_information.py: WMI is not found: Ignore if using Linux')
    found_wmi = False

# CPU cores
def core_count0():
    cpu_count = psutil.cpu_count(logical = True) #important to keep on True
    cpu_list = [i for i in range(cpu_count)]
    return cpu_list

# return just how many cores there are without extra info
def returnCores():
    return psutil.cpu_count(logical=True)

# CPU Logical cores (for Hyperthreading)
#def core_count1():
#    return psutil.cpu_count(logical = True)

def get_load():
    return psutil.cpu_percent(None, True) #get cpu load per core

# Current cpu freq
def cpu_freq():
    '''Take out information from psutil.cpu_freq and return it as a 2d list, 
    the info in cpu_freq is garbled up and this essentially seperates it and cleans it up for easier access'''
    cpu_freq_decoded = psutil.cpu_freq(percpu=True)
    core = []
    coretemp = []
    for index in range(len(cpu_freq_decoded)):
        for j in range(0,3): #0 is current, 1 is min, 2 is max
            coretemp.append(cpu_freq_decoded[index][j]) #cpu_freq_decoded[index][j], index is core, j is temp type
        core.append(coretemp)
        coretemp = []
    return core #returns 2d array of [core] and [temp]

# Current CPU Untilization (Usage)
def cpu_usage():
    return psutil.cpu_percent(interval = 1, percpu=True)

# CPU Tempature (measured in celsius)
def cpu_temperature():
        try:
            cpu_temperature = psutil.sensors_temperatures()
        except:
            temp = [random.randrange(1, 100) for _ in range(3)] #generate fake ones
            temp.sort()
            return temp 
        temp = []
        if (cpu_temperature == {}): #psutil didn't find any values
            temp = [random.randrange(1, 100) for _ in range(3)] #generate fake ones
            temp.sort()
            return temp 
        
        for key, val in cpu_temperature.items():
            for temperature in val:
                temp.append(str(temperature[1]))
                temp.append(str(temperature[2]))
                break
        return temp

def cpu_name():
    return cpuinfo.get_cpu_info()['brand_raw']
