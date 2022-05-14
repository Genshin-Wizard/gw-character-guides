import json
import os

characters = json.load(open("character_guides.json", "r"))

for character in characters:
    os.mkdir(character)