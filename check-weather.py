#
# check-weather.py
#
# by - sam nnodim
#
# adapted from: https://github.com/mikedewar/RealTimeStorytelling

# import some v useful libs
from sys import stdout
import requests
import json
import time
import random as r

# this script polls the soundcloud API, looking for new songs uploaded to
# the platform.

listofSongs = {}
url = "http://api.openweathermap.org/data/2.5/weather?zip=10025,us&appid="
apikey = "2df8905bba963ddd6ffe981af70669fb" # OpenWeatherMap API key

while True:
    # send a GET request to the OWM API and turn it to JSON data
    data = requests.get( url + apikey ).json()

    # Get weather params from data
    print ( json.dumps(data) )

    # sleep for 2 mins and poll again
    time.sleep( 120 )
