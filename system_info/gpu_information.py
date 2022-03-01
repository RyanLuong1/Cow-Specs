import platform
import GPUtil

# GPU Information
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
