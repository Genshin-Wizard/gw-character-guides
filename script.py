import json

characters = json.load(open("character_guides.json", "r"))

for character in characters:
    with open(f'{character}.json', 'w', encoding='utf-8') as f:
        json.dump(characters[character], f, ensure_ascii=False, indent=4)