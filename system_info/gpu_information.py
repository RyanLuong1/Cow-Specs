import platform
import gputil

# GPU Information
# GPU ID: Displays which gpu is installed on PCIE slot
def gpu_id():
    return gputil.id

# GPU Name
def gpu_name():
    return gputil.name

# GPU Utilization
def gpu_usage():
    return gputil.showUtilization()

# GPU Free Memory
# This wont show each gpu usage
def gpu_free_mem():
    return gputil.memoryFree

# GPU Used Memory
def gpu_used_mem():
    return gputil.memoryUsed

# GPU Total Memory
def gpu_mem():
    return gputil.memoryTotal

# GPU Tempature (measured in celsius)
def gpu_temp():
    return gputil.tempature
