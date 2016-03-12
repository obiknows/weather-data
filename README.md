:umbrella: weather-data :umbrella:
==========================================


This data stream acquired using the
[The Dark Sky Forecast API](https://developer.forecast.io/)
polls the API every minute to grab the distance of the nearest storm to Columbia University (rel. to [Butler Library](https://en.wikipedia.org/wiki/Butler_Library))  and stores that in a redis store. At the same time,
on every entry on the redis store, we calculate a moving average of the
air pressure and we send an alert via twitter, alerting us of the chance
of rain.


### Usage (TBD)

1. Install 
2. In one tab start an instance of redis: 
		
		redis-server
3. In another run the command:

		./pipeline.sh
4. Observe the Twitter account: [@fd]()
5. Bask in the beauty of the notifications