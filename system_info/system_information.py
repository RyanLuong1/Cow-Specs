import platform
import psutil

## System information

# Total Ram installed on the system
# rounds to the nearest decimal place (needs to be double checked)
def total_ram():
    return {round(psutil.virtual_memory().total/1000000000000, 2)}

# Avaliable Ram
def avaliable_ram():
    return {round(psutil.virtual_memory().avaliable/1000000000000, 2)}

# Used Ram
# {round(psutil.virtual_memory().used/1000000000000, 2)}

# Ram Untilization
def memory_usage():
    return {psutil.virtual_memory().percent}
