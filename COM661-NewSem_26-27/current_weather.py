import datetime
import json
import urllib.request

def url_builder(lat, lon):
    api = "0b3bdd00fa307fd362a0bce74e85ccf7"
    unit = 'metric'
    
    return 'https://api.openweathermap.org/data/2.5/weather'+ \
        '?units=' + unit + \
        '&appid=' + api + \
        '&lat=' + str(lat) + \
        '&lon=' + str(lon)
        
def fetch_data(full_url):
    url = urllib.request.urlopen(full_url)
    output = url.read().decode('utf-8')
    return json.loads(output)

def time_converter(timestamp):
    return datetime.datetime.fromtimestamp(timestamp). \
        strftime('%d %b %I:%M %p')
        
lat = 51.5074
lon = -0.1278

json_data = fetch_data(url_builder(lat,lon))

temperature = str(json_data['main']['temp'])
timestamp = time_converter(json_data['dt'])
description = json_data['weather'][0]['description']

print(json_data)
print("Current Weather")
print(timestamp + " : " + temperature + " : " + description)