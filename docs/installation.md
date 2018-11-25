* Install MariaDB

* Create user aqpi

```sql
CREATE USER 'aqpi'@'localhost' IDENTIFIED BY 'password'; 
```

* Create database AQpi

```sql
 CREATE DATABASE AQpi;
```

* Grant all priviledges on AQpi DB to aqpi user

```sql
 GRANT ALL PRIVILEGES ON AQpi.* TO 'aqpi'@'localhost';
```

* Create table air_quality

```sql
 CREATE TABLE air_quality(
 `id` int AUTO_INCREMENT,
 `current_time` DATETIME,
 `temp` FLOAT,
 `rh` FLOAT,
 `pm2_5` FLOAT,
 `pm10` FLOAT,
 `so2` FLOAT,
 `no2` FLOAT,
 `o3` FLOAT,
 `co` FLOAT,
 PRIMARY KEY ( id ) 
 );
```

