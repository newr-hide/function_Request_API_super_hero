import requests
from pprint import pprint

def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    url = "https://akabab.github.io/superhero-api/api"
    response = requests.get(f'{url}/all.json')
    #pprint(response.json())

    # with open('image_name.json', "w") as file:
    #     file.write(response.text)
    all_hero_info = response.json()
    tmp_dict = {}
    for hero_info in all_hero_info:
        if hero_info["name"] == "Hulk":
            tmp_dict["Hulk"] = hero_info["powerstats"]['intelligence']
        if hero_info["name"] == "Captain America":
            tmp_dict["Captain America"] = hero_info["powerstats"]['intelligence']
        if hero_info["name"] == "Thanos":
            tmp_dict["Thanos"] = hero_info["powerstats"]['intelligence']




    #print(max(tmp_dict))


    return max(tmp_dict)


print(get_the_smartest_superhero())