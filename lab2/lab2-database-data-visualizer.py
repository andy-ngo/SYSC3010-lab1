#this will be used to visualize the data from the sensor data table db file
import sqlite3
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import datetime

#connect to the file that will be used for plotting
dbconnect = sqlite3.connect("sensorDB.db")

#initialize a plot with a secondary y axis
plt = make_subplots(specs=[[{"secondary_y":True}]])

#read from the sql file
data = pd.read_sql_query("SELECT * FROM sensordata",dbconnect)

#plot the data as scatter
plot = px.scatter(data,x = 'datetime',y = ['temperature','humidity'])
#plot on secondary axis
plot2 = px.scatter(data, x = 'datetime',y = ['pressure'])
plot2.update_traces(yaxis = 'y2', marker = dict(color='yellow'))

#add plots together
plt.add_traces(plot.data + plot2.data)
#create titles
plt.layout.title = "Sensor Over Time"
plt.layout.xaxis.title = "DateTime[H:M:S:D]"
plt.layout.yaxis.title = "Temperature(C) and Humidity(%)"

#add in another yaxis for the pressure
plt.layout.yaxis2.type = "log"
plt.layout.yaxis2.title = "Pressure(millibars)"

#display plot
plt.show()