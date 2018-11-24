from AM2315 import AM2315
import time

sensor=AM2315()

while 1 == 1:
#Set variables to None so that we don't have false data if there is an issuew with the sensor.
    current_time = None
    temp = None
    rh = None
    pm = None
    so2 = None
    no2 = None
    o3 = None
    co = None

    current_time = time.time()
    temp = sensor.temperature()
    rh = sensor.humidity()

    print([current_time, temp, rh])
    time.sleep(5)


exit()
