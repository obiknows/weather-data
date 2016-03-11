#
# check-weather.py
#
# by - sam nnodim
#
# adapted from: https://github.com/mikedewar/RealTimeStorytelling

# import some very useful libs
from sys import stdout
import requests
import json
import time
import random as r

# this script polls the soundcloud API, looking for new songs uploaded to
# the platform.

url = "http://api.openweathermap.org/data/2.5/weather?id=4900961&appid="
apikey = "b1b15e88fa797225412429c1c50c122a" # OpenWeatherMap API key

while True:
    # send a GET request to the OWM API and turn it to JSON data
    data = requests.get( url + apikey ).json()

    # get the humidity from the data
    humidity = data["main"]["humidity"]

    # Get weather params from data
    print ( json.dumps(data) )

    # sleep for 2 mins and poll again
    time.sleep( 120 )
