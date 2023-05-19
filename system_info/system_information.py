import platform
import psutil
from psutil._common import bytes2human

## System information

# Total Memory installed on the system (in GB)
def total_ram():
    return round(psutil.virtual_memory().total/1000000000)

# Avaliable Memory (in GB with 2 decimal places)
def avaliable_ram():
    return round(psutil.virtual_memory().available/1000000000, 2)

# Memory Untilization (in percentage)
def memory_usage():
    return psutil.virtual_memory().percent

# Memory Temperature
#def memory_temperature():
#    return psutil.virtual_memory  



# Storage information
# Displays all partitions in system 
def disk_count():
    return len(psutil.disk_partitions(False))

def disk_partition():
    disks = psutil.disk_partitions(False)
    disk_directory = []
    for i in range(len(disks)):
        disk_directory.append(disks[i][0])
    return disk_directory

# Fan speed
def fan_speed():
    if psutil.sensors_fans() > 0:
        return psutil.sensors_fans()
    else:
        return "Not available"



## Networking information

# Returns IPv4 (32bit IP Address)
def network_IPv4():
    return psutil.net_connections(kind='inet4')

# Returns IPv6 (64bit IP Address)
def network_IPv6():
    return psutil.net_connections(kind='inet6')

# Returns IPv4 over TCP 
def network_IPv4_TCP():
    return psutil.net_connections(kind='tcp4')

# Returns IPv6 over TCP 
def network_IPv6_TCP():
    return psutil.net_connections(kind='tcp6')


## Network Traffic

# Number of ingoing packets

# Number of outgoing packets
