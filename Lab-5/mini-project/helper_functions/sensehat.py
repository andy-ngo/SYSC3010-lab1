from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#This function returns a SenseHat instance
def get_sensehat():
    return sense

#This function takes in a SenseHat instance and the flash_time
#The display on the SenseHat flases red (1 second on, 1 second off) for the duration of
#flash_time. At the end of the flash_time the SenseHat display should be off.
def alarm(sense,flash_time):
    for i in range(flash_time):
        sense.clear(255,0,0)
        sleep(1)
        sense.clear(0,0,0)
        sleep(1)
