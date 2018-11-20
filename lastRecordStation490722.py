from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'
weather = get(url).json()
weather['items']
last_record = weather['items'][-1]
print (last_record)