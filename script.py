import json, os

characters = json.load(open("!character_guides.json", "r"))

for character in characters:
    os.mkdir(character)
    files = ['introduction', 'build', 'playstyle', 'ascension', 'synergies', 'constellations']
    for file in files:
        with open(f'{character}/{file}.json', 'w', encoding='utf-8') as f:
            json.dump(characters[character], f, ensure_ascii=False, indent=4)