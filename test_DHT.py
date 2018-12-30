#!/usr/bin/python3
import sys
import Adafruit_DHT as adht

sensor = 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 22 # 2302 # sensor is the AM2302. could be DHT11 or DHT22, in which case, use 11,22. 

while True:
    humidity, tempC = adht.read_retry(sensor,4)
    print('Temp [C] = {0:0.1f} , Humidity = {1:0.1f} %'.format(tempC,humidity)) 
