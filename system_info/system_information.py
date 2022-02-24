import platform
import psutil
import gputil   # only works for Nvidia GPU

# Need to find GPU information 
# Need to find Motherboard information

## System information


# Computer Network name
# Example "DESKTOP-54OI004"
comp_plat = {platform.node()}

# Processor type
# Example "Intel64 Family..."
cpu_type = {platform.processor()}

# Operating System
operating_system = {platform.system}

# Operating System Version
operating_system_version = {platform.version()}


# CPU physical cores
core_count0 = {psutil.cpu_count(logical = False)}

# CPU Logical cores (for Hyperthreading)
core_count1 = {psutil.cpu_count(logical = True)}

# Current CPU Frequency
cpu_freq = {psutil.cpu_freq().current}

# Minimum CPU Frequency
cpu_freq_min = {psutil.cpu_freq().min}

# Maximum CPU Frequency
cpu_fre_max = {psutil.cpu_freq().max}

# Current CPU Untilization (Usage)
cpu_usage = {psutil.cpu_percent(interval = 1)}

# CPU Tempature (measured in celsius)
#cpu_temp = 


# Total Ram installed on the system
# rounds to the nearest decimal place (needs to be double checked)
{round(psutil.virtual_memory().total/1000000000000, 2)}

# Avaliable Ram
{round(psutil.virtual_memory().avaliable/1000000000000, 2)}

# Used Ram
# {round(psutil.virtual_memory().used/1000000000000, 2)}

# Ram Untilization
{psutil.virtual_memory().percent}


# GPU Information
# GPU ID: Displays which gpu is installed on PCIE slot
gpu_id = gputil.id

# GPU Name
gpu_name = gputil.name

# GPU Utilization 
gpu_usage = gputil.showUtilization()

# GPU Free Memory
# This wont show each gpu usage
gpu_free_mem = gputil.memoryFree

# GPU Used Memory
gpu_used_mem = gputil.memoryUsed

# GPU Total Memory
gpu_mem = gputil.memoryTotal

# GPU Tempature (measured in celsius)
gpu_temp = gputil.tempature
