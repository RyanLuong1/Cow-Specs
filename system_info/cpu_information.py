import platform
import psutil

# CPU physical cores
def core_count0():
    return {psutil.cpu_count(logical = False)}

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
    return {psutil.sensors_temperatures()}