import requests
import json

if __name__ == '__main__':
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    response = requests.get(url + '/all.json')
    heroes = json.loads(response.text)
    heroes_intelligence = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
    for hero in heroes:
        if hero['name'] in heroes_intelligence.keys():
            heroes_intelligence[hero['name']] = hero['powerstats']['intelligence']
    print(max(heroes_intelligence, key=lambda key: heroes_intelligence[key]))

