from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'
weather = get(url).json()
weather['items']
first_record = weather['items'][0]
print (first_record)