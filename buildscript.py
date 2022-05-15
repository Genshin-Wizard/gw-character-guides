import json, os, discord, requests

characters = json.load(open("character_guides.json", "r"))
icon = json.load(open("avatars.json", "r"))['data']

def elementColor(element):
    return {
        'Dendro':'6794623', 
        'Hydro':'3245055', 
        'Anemo':'5494962', 
        'Geo':'14994176', 
        'Pyro':'16733525', 
        'Cryo':'10147839', 
        'Electro':'11104511'
    }.get(str(element))
    
def getBanner(element):
    return {
        'Dendro':'https://i.imgur.com/tdg9kqt.png', 
        'Hydro':'https://i.imgur.com/KJbeHEM.png', 
        'Anemo':'https://i.imgur.com/nSL3fPX.png', 
        'Geo':'https://i.imgur.com/XlWnH6g.png', 
        'Pyro':'https://i.imgur.com/X8lPFdK.png', 
        'Cryo':'https://i.imgur.com/uzxtSoN.png', 
        'Electro':'https://i.imgur.com/56WmQ8I.png'
    }.get(str(element))

def elementEmoji(element):
    return {
        'Dendro':'<:Dendro:951729014106628106>', 
        'Hydro':'<:Hydro:951729014249234442>', 
        'Anemo':'<:Anemo:951729013859155979>', 
        'Geo':'<:Geo:951729014094065674>', 
        'Pyro':'<:Pyro:951729013804650507>', 
        'Cryo':'<:Cryo:951729013674623017>', 
        'Electro':'<:Electro:951729014165344278>'
    }.get(str(element))

def getRarity(rarity):
    return {
        '5':'★★★★★', 
        '4':'★★★★', 
        '3':'★★★', 
    }.get(str(rarity))

for character in characters:
    print(character)

    embed = discord.Embed(
        title = f'{character.capitalize()} | Build',
        color = int(characters[character]['color']),
    )
    footer =  {
        "footer": {
            "text": f"Character Guide • Build: {character.capitalize()}"
        }
    }
    title = {
        "title": f"{characters[character]['title']} | Build"
        }

    characters[character].update(footer)
    characters[character].update(title)
    with open(f'{character}/build.json', 'w', encoding='utf-8') as f:
        json.dump(characters[character], f, ensure_ascii=False, indent=4)