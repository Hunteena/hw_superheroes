import requests


def most_intelligent_superhero(names):
    token = '2619421814940190'
    intelligences = []
    for name in names:
        url = f'https://superheroapi.com/api/{token}/search/{name}'
        response = requests.get(url=url)
        hero_intelligence = response.json()['results'][0]['powerstats']['intelligence']
        intelligences.append(int(hero_intelligence))
    most_intelligent = names[intelligences.index(max(intelligences))]
    return most_intelligent


if __name__ == '__main__':
    names = ['Hulk', 'Captain America', 'Thanos']
    print(f'Самый умный - {most_intelligent_superhero(names)}')
