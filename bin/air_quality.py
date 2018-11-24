from AM2315 import AM2315
import time

sensor=AM2315()

while 1 == 1:
#Set variables 
    time = None
    temp = None
    rh = None
    pm = None
    so2 = None
    no2 = None
    o3 = None
    co = None

    time = time.time()
    temp = sensor.temperature()
    rh = sensor.humidity()

    print([time, temp, rh])

exit()
