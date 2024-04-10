import requests
from pprint import pprint

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    url = "https://akabab.github.io/superhero-api/api"
    response = requests.get(f'{url}/all.json')
    pprint(response.json())

    with open('image_name.json', "w") as file:
        file.write(response.text)
    return the_smartest_superhero


print(get_the_smartest_superhero())