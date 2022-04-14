import platform
import GPUtil
import random


# GPU Information
GPU = GPUtil.getGPUs()

# GPU Name
def gpu_name():
    return GPU[0].name if GPU else "GPU"

# GPU Utilization
def gpu_usage():
    return GPU[0].load*100 if GPU else random.randint(1, 100)

# GPU Tempature (measured in celsius)
def gpu_temp():
    return GPU[0].temperature if GPU else random.randint(1, 100)
