#will be used to read temperature, humidity, and pressure data from the SenseHat sensor once per second and puts it
#into the table in the db file.
from sense_hat import SenseHat
import sqlite3
import time
import datetime

sense = SenseHat()
id = 0

#connect to database file
dbconnect = sqlite3.connect("sensorDB.db")

dbconnect.row_factory = sqlite3.Row

cursor = dbconnect.cursor()

#for loop will be used to keep tracking data, the range will be set as 1000
for i in range(10):
	id += 1
	dt = datetime.datetime.now()
	temp = round(sense.get_temperature(),1)
	humidity = round(sense.get_humidity,1)
	pressure = round(sense.get_pressure,1)
	#will put the data just collected into the table in the db file
	cursor.execute('''insert into sensordata values(?,?,?,?,?)''',(id,dt,temp,humidity,pressure))
	time.sleep(1)

dbconnect.commit()


#will select the data that was just placed in the table to print it out
cursor.execute('SELECT * FROM sensordata')
#print data

for row in cursor:
    print(row['id'],row['datetime'],row['temperature'],row['humidity'],row['pressure'])

dbconnect.close()
