* Install MariaDB

* Create user aqpi

 CREATE USER 'aqpi'@'localhost' IDENTIFIED BY 'password'; 

* Create database AQpi

 CREATE DATABASE AQpi;

* Grant all priviledges on AQpi DB to aqpi user

 GRANT ALL PRIVILEGES ON AQpi.* TO 'aqpi'@'localhost';

* Create table air_quality

 CREATE TABLE air_quality( `id` int AUTO_INCREMENT, `current_time` DATETIME, `temp` FLOAT, `rh` FLOAT, `pm2_5` FLOAT, `pm10` FLOAT, `so2` FLOAT, `no2` FLOAT, `o3` FLOAT, `co` FLOAT, PRIMARY KEY ( id ) );


