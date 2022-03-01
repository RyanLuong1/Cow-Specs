import platform
import psutil
import GPUtil   # only works for Nvidia GPU

# Need to find GPU information
# Need to find Motherboard information

## System information


# Computer Network name
# Example "DESKTOP-54OI004"
def computer_platform():
    return {platform.node()}

# Processor type
# Example "Intel64 Family..."
def cpu_type():
    return {platform.processor()}

# Operating System
def operating_system():
    return {platform.system()}

# Operating System Version
def operating_system_version():
    return {platform.version()}


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
#cpu_temp =


# Total Ram installed on the system
# rounds to the nearest decimal place (needs to be double checked)
def total_ram():
    return {round(psutil.virtual_memory().total/1000000000000, 2)}

# Avaliable Ram
<<<<<<< HEAD
def avaliable_ram():
    return {round(psutil.virtual_memory().avaliable/1000000000000, 2)}
=======
{round(psutil.virtual_memory().available/1000000000000, 2)}
>>>>>>> dd95877c4e2c6d41af1b262397040ef2bf568f70

# Used Ram
# {round(psutil.virtual_memory().used/1000000000000, 2)}

# Ram Untilization
def memory_usage():
    return {psutil.virtual_memory().percent}


# GPU Information

# GPUs Declaration
GPUs = GPUtil.getGPUs()
# GPU ID: Displays which gpu is installed on PCIE slot

def gpu_id():
    return GPUtil.id

# GPU Name
def gpu_name():
    return GPUtil.name

# GPU Utilization
def gpu_usage():
    return GPUtil.showUtilization()

# GPU Free Memory
# This wont show each gpu usage
def gpu_free_mem():
    return GPUtil.memoryFree

# GPU Used Memory
def gpu_used_mem():
    return GPUtil.memoryUsed

# GPU Total Memory
def gpu_mem():
    return GPUtil.memoryTotal

# GPU Tempature (measured in celsius)
def gpu_temp():
    return GPUtil.temperature
