#
# check-weather.py
#
# by - sam nnodim
#
# adapted from: https://github.com/mikedewar/RealTimeStorytelling

# import some very useful libs
from sys import stdout
import numpy as np
import requests
import json
import time

# this script polls the soundcloud API, looking for new songs uploaded to
# the platform.

url = "http://api.openweathermap.org/data/2.5/weather?id=4900961&appid="
apikey = "b1b15e88fa797225412429c1c50c122a" # OpenWeatherMap API key

# Set poission param. (2 minutes)
rate = 60

while True:
    # send a GET request to the OWM API and turn it to JSON data
    data = requests.get( url + apikey ).json()

    # get the pressure from the data
    pressure = data["main"]["pressure"]

    # Print current weather pressure from params
    print ( json.dumps({"pressure": pressure}) )
    stdout.flush()

    # set the sleep rate as a randomn exponential value
    # draw time beteween events from a random distribution
    time.sleep( np.random.exponential(rate) )
