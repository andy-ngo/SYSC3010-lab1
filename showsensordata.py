from sense_hat import SenseHat

sense = SenseHat()
blue = (0,0,255)
yellow = (255,255,0)

while True:
    temp = sense.get_temperature()
    pres = sense.get_pressure()
    hum = sense.get_humidity()
    
    temp = round(temp,1)
    pres = round(pres,1)
    hum = round(hum,1)
    
    sensordata = "T:" + str(temp) + " P:" + str(pres) + " H:" + str(hum)
    
    sense.show_message(sensordata,text_colour = yellow, back_colour = blue, scroll_speed = 0.1)

