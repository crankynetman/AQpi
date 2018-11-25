from AM2315 import AM2315
import mysql.connector as mariadb
import time
import os
from configparser import ConfigParser

file_path = os.path.dirname(__file__)
if file_path != "":
    os.chdir(file_path)

parser = ConfigParser()
parser.read('../config/aqpi_config.py')

db_user = parser.get('mysql', 'user')
db_password = parser.get('mysql', 'password')
db_host = parser.get('mysql', 'host')
db_name = parser.get('mysql', 'name')

mariadb_connection = mariadb.connect(\
    user=db_user, password=db_password, host=db_host, database=db_name, autocommit=True\
)
cursor = mariadb_connection.cursor(buffered=True)

sensor=AM2315()


while 1 == 1:
    #Set variables to None so that we don't have false data if there is an issue with the sensor.
    current_time = None
    temp = None
    rh = None
    pm2_5 = None
    pm10 = None
    so2 = None
    no2 = None
    o3 = None
    co = None

    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    temp = sensor.temperature()
    rh = sensor.humidity()

    cursor.execute(\
        "INSERT INTO air_quality (\
            `current_time`, `temp`, `rh`, `pm2_5`, `pm10`, `so2`, `no2`, `o3`, `co`) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
            (current_time, temp, rh, pm2_5, pm10, so2, no2, o3, co)\
        )

    time.sleep(5)


exit()
