import random
import math

class Sensor:
    def __init__(self):
        pass
    
    def Sensor_1(self):
        temp = random.randint(25,45)
        return temp
    
    def Sensor_2(self):
        spe = random.randint(1,80)
        return spe
    
    def Sensor_3(self):
        rpm = random.randint(0,7)
        return rpm
    
    def Sensor_4(self):
        range = 30
        return range
    
    def Sensor_5(self):
        battery_perc = 95
        return battery_perc
        


