'''
Created on Mar 8, 2019

@author: blossom
'''

import psutil
from Processes import Processes
import time

class MetricsCollector:
    
    logicalCPUSs = 0
    physicalCPUs = 0
    
    def __init__(self):
        #self.cpuTime()
        #self.percent()
        logicalCPUs = psutil.cpu_count(logical = True)
        physicalCPUSs = psutil.cpu_count(logical = False)
        print("Logical CPUS: " + str(logicalCPUs))
        print("Physical CPUS: " + str(physicalCPUSs))
       # self.diskinfo()        
    
    def cpuTime(self):

        cputime = psutil.cpu_times(True)
        for time in cputime:
            print(time)
        
    def percent(self):
        count = 1
        while(count > 0):
            # Setting percpu=false will average, true is all
            percent = psutil.cpu_percent(interval=1, percpu=True)
            print(percent)
            count-=1
            
    def stats(self):
        stats = psutil.cpu_stats()
        print(stats)
        
    def diskinfo(self):
        print(psutil.disk_partitions())
        for mount in psutil.disk_partitions():
            print(mount[1],mount[2]) # prints the mount point
            print(psutil.disk_usage(mount[1])[2]) # prints disk free space
        
proc = Processes()

while True:
    proc.updateDatabase()
    time.sleep(10)