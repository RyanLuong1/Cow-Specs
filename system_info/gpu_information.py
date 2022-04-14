import platform
import GPUtil
import logging
import random


# GPU Information
try:
    GPU = GPUtil.getGPUs()
except:
    logging.warning("Only Nvidia Gpus are supported for GPU monitoring")

# GPU Name
def gpu_name():
    try: 
        return GPU[0].name if GPU else "GPU" 
    except:
        pass

# GPU Utilization
def gpu_usage():
    try: 
        return GPU[0].load*100 if GPU else random.randint(1, 100)
    except: pass
   

# GPU Temperature (measured in celsius)
def gpu_temp():
    try: 
        return GPU[0].temperature if GPU else random.randint(1, 100)
    except:
        pass
   