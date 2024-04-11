import requests
from pprint import pprint

def get_the_smartest_superhero(superheros) -> int:
    url = "https://akabab.github.io/superhero-api/api"
    response = requests.get(f'{url}/all.json')
    all_hero_info = response.json()
    tmp_dict = {}
    tmp_dict_2 = {}
    for hero_info in all_hero_info:
        if hero_info["id"] in superheros:
            tmp_dict[hero_info["id"]] = hero_info["powerstats"]['intelligence']
            tmp_dict_2[hero_info["id"]] = hero_info["name"]
    hero = max(tmp_dict,key=tmp_dict.get)


    return tmp_dict_2[hero]





print(get_the_smartest_superhero([35, 69, 104, 149]))