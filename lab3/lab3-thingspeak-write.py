from sense_hat import SenseHat
import requests
import time
import json

sense = SenseHat()

sendKey = "D1PXFM6VKZFYETUG"
url = "https://api.thingspeak.com/update"

posting_interval = 120

def main():
    sense = SenseHat()
    temperature = round(sense.get_temperature(),1)
    humidity = round(sense.get_humidity(),1)
    pressure = round(sense.get_pressure(),1)

    # payload includes the headers to be sent with the GET request
    # read the documentation for more information (https://docs.python-requests.org)
    payload = {'field1':temperature,'field2':humidity,'field3':pressure,'api_key':sendKey}
    try:
        # Sends an HTTP GET request
        response = requests.get(url, params=payload)
        response = response.json()

        print(response)
        time.sleep(posting_interval)
    except:
        print("Connection Failed")

if __name__ == "__main__":
    while True:
        main()


