import pyrebase
import random
import time
from sense_hat import SenseHat

sense = SenseHat()

config = {
	"apiKey": "AIzaSyBIJ2jpYTR7_FjCgvXpykUUaWUIotIDL7w",
	"authDomain": "SYSC3010-Ngo-Andy.firbaseapp.com",
	"databaseURL": "https://sysc3010-ngo-andy-default-rtdb.firebaseio.com/",
	"storageBucket": "SYSC3010-Ngo-Andy.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataset1 = "temperature"
dataset2 = "humidity"
dataset3 = "pressure"

def writeData():
    
    config = {
	"apiKey": "AIzaSyBIJ2jpYTR7_FjCgvXpykUUaWUIotIDL7w",
	"authDomain": "SYSC3010-Ngo-Andy.firbaseapp.com",
	"databaseURL": "https://sysc3010-ngo-andy-default-rtdb.firebaseio.com/",
	"storageBucket": "SYSC3010-Ngo-Andy.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    dataset1 = "temperature"
    dataset2 = "humidity"
    dataset3 = "pressure"
    
    key = 1

    while True:
        temp = round(sense.get_temperature(),1)
        hum = round(sense.get_humidity(),1)
        pres = round(sense.get_pressure(),1)

        db.child(dataset1).child(key).set(temp)
        db.child(dataset2).child(key).set(hum)
        db.child(dataset3).child(key).set(pres)

        key = key + 1
        time.sleep(120)

def readData():
    
    config = {
    "apiKey": "AIzaSyC8fl5pbVfvZfKwlLd7opcfgDFJZBEDYt8",
    "authDomain": "sandbox-49b77.firbaseapp.com",
    "databaseURL": "https://sandbox-49b77-default-rtdb.firebaseio.com/",
    "storageBucket": "sandbox-49b77.appspot.com"
    }
    
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    dataset1 = "Temperature"
    dataset2 = "Humidity"
    dataset3 = "Pressure"
    
    mySensorData1 = db.child(dataset1).get()
    mySensorData2 = db.child(dataset2).get()
    mySensorData3 = db.child(dataset3).get()
    
    mySensorData1_list = mySensorData1.each()
    mySensorData2_list = mySensorData2.each()
    mySensorData3_list = mySensorData3.each()

    lastDataPoint_T = mySensorData1_list[-1]
    secondDataPoint_T = mySensorData1_list[-2]
    thirdDataPoint_T = mySensorData1_list[-3]
    
    lastDataPoint_H = mySensorData2_list[-1]
    secondDataPoint_H = mySensorData2_list[-2]
    thirdDataPoint_H = mySensorData2_list[-3]

    lastDataPoint_P = mySensorData3_list[-1]
    secondDataPoint_P = mySensorData3_list[-2]
    thirdDataPoint_P = mySensorData3_list[-3]

    print("Temperature Key: {}, {}, {}".format(len(mySensorData1_list)-1,len(mySensorData1_list)-2,len(mySensorData1_list)-3))
    print("Temperature Value: {}, {}, {}\n".format(lastDataPoint_T.val(),secondDataPoint_T.val(),thirdDataPoint_T.val()))
    
    print("Humidity Key: {}, {}, {}".format(lastDataPoint_H.key(),secondDataPoint_H.key(),thirdDataPoint_H.key()))
    print("Humidity Value: {}, {}, {}\n".format(lastDataPoint_H.val(),secondDataPoint_H.val(),thirdDataPoint_H.val()))
    
    print("Pressure Key: {}, {}, {}".format(lastDataPoint_P.key(),secondDataPoint_P.key(),thirdDataPoint_P.key()))
    print("Pressure Value: {}, {}, {}\n".format(lastDataPoint_P.val(),secondDataPoint_P.val(),thirdDataPoint_P.val()))

if __name__ == "__main__":
    #writeData()
    readData()
