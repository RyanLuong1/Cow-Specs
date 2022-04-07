import platform
import GPUtil
import logging

# GPU Information
try:
    GPU = GPUtil.getGPUs()[0]
except:
    logging.warning("Only Nvidia Gpus are supported for GPU monitoring")

# GPU Name
def gpu_name():
    try: 
        return GPU.name 
    except:
        pass

# GPU Utilization
def gpu_usage():
    try: 
        return GPU.load*100
    except: pass

# GPU Tempature (measured in celsius)
def gpu_temp():
    try: 
        return GPU.temperature
    except:
        pass
