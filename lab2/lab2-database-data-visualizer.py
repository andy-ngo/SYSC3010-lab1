#this will be used to visualize the data from the sensor data table db file
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import dates as mpl_dates
import datetime

dbconnect = sqlite3.connect("sensorDB.db")

dbconnect.row_factory = sqlite3.Row

cursor = dbconnect.cursor()
cursor.execute('SELECT * FROM sensordata')

#creating the secondary y-axis
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

#format the datetime into hours-minutes-seconds
data = pd.read_sql_query('SELECT * FROM sensordata', dbconnect)
data['datetime'] = pd.to_datetime(data['datetime'])
data.sort_values('datetime', inplace=True)
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('H%-%M-%S')
plt.gca().xaxis.set_major_formatter(date_format)

#the labels for the plot
ax1.set_xlabel("Time[H:M:S]")
ax1.set_ylabel("Temperature(°C),Humidity(%)")
ax2.set_ylabel("Pressure(millibars)")
plt.title("Sensor over time")

#setting up variables
temp = data['temperature']
hum = data['humidity']
pres = data['pressure']

#plotting the points and giving them marks and labels
plt.plot(data['datetime'],temp,color = 'red',marker='o',label = "Temperature(°C)")
plt.plot(data['datetime'],hum,color = 'yellow',marker='o',label = "Humidity(%)")
plt.plot(data['datetime'],pres,color = 'blue',marker='o',label = "Pressure(millibars)")

ax1.plot(data['datetime'],temp,color = 'red',marker='o')
ax1.plot(data['datetime'],hum,color = 'yellow',marker='o')
ax2.plot(data['datetime'],pres,color = 'blue',marker='o')

#display legend and setup as tight layout
plt.legend()
plt.tight_layout()
plt.show()
dbconnect.close()
