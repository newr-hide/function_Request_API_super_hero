import requests
from pprint import pprint
import time

def find_uk_city(coordinates:list) -> str:
    uk_cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    city_ =[]
    for coordinat in coordinates:
        lat = coordinat[0]
        lon = coordinat[1]

        url ='https://geocode.maps.co/reverse'
        params = {
        'lat': lat,
        'lon': lon,
        'api_key': '6619f853cb4b5992104642dogfc5dfd'
        }
        response = requests.get(url, params=params)
        tmp_var = response.json()['address']

        city = tmp_var.get('city')
        city_.append(city)
        time.sleep(1)
    for i in city_:
        if i in uk_cities:
            print(i)



print(find_uk_city([
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]))