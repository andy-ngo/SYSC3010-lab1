from sense_hat import SenseHat
import requests
import json
import time

sense = SenseHat()
white = (0,0,0)
black = (255,255,255)
readKey = "MH6TCXDYXCKZ09FB"
channelNumber = "1642126"
url = "https://api.thingspeak.com/channels/" + channelNumber + "/feeds.json"
results = 3

def main():
    payload = {'api_key': readKey, 'results': results}

    response = requests.get(url, params=payload)
    response = response.json()

    print("Channel Name: {}".format(response['channel']['name']))

    entries = response['feeds']

    for e in entries:
        responsedata = "T:" + str(e['field1']) + " H:" + str(e['field2']) + " P:" + str(e['field3'])
        sense.show_message(responsedata,text_colour = black,back_colour = white, scroll_speed = 0.1)
        print("At {}, the temperature was {}".format(e['created_at'],e['field1']))
        print("At {}, the humidity was {}".format(e['created_at'],e['field2']))
        print("At {}, the pressure was {}".format(e['created_at'],e['field3']))

if __name__ == "__main__":
    main()
