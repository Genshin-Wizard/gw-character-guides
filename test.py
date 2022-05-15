import json, os

characters = json.load(open("data.json", "r"))

# klee = characters['klee']
footer =  {
    "footer": {
        "text": "Character Guide • Introduction: Klee"
    }
}
characters.update(footer)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(characters, f, ensure_ascii=False, indent=4)
