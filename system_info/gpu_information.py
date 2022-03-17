import platform
import GPUtil


# GPU Information
GPU = GPUtil.getGPUs()[0]

# GPU Name
def gpu_name():
    return GPU.name 

# GPU Utilization
def gpu_usage():
    return GPU.load*100

# GPU Tempature (measured in celsius)
def gpu_temp():
    return GPU.temperature
