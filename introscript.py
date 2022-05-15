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
        '5':'<:5Star:954093937109401620> <:5Star:954093937109401620> <:5Star:954093937109401620> <:5Star:954093937109401620> <:5Star:954093937109401620>', 
        '4':'<:4Star:954095346051608616>  <:4Star:954095346051608616>  <:4Star:954095346051608616>  <:4Star:954095346051608616> ', 
        '3':'<:3Star:954093937092599808> <:3Star:954093937092599808> <:3Star:954093937092599808>', 
    }.get(str(rarity))

for character in characters:
    temp = character
    temp2 = character
    if character == 'geotraveler':
        character = 'traveler-geo'
        temp = 'traveler'
    elif character == 'anemotraveler':
        character = 'traveler-anemo'
        temp = 'traveler'
    elif character == 'electrotraveler':
        character = 'traveler-electro'
        temp = 'traveler'
    elif character == 'ayato':
        continue
    elif character == 'itto':
        continue
    elif character == 'yelan':
        continue
    elif character == 'kuki':
        continue
    elif character == 'childe':
        character = 'tartaglia'
    elif character == 'hutao':
        character = 'hu-tao'
    elif character == 'yaemiko':
        character = 'yae-miko'
    elif character == 'yunjin':
        character = 'yun-jin'
    print(character)
    r = requests.get(f'https://api.genshin.dev/characters/{character}')
    data = json.loads(r.text)


    embed = discord.Embed(
        title = data['name'],
        color = int(elementColor(data['vision'])),
        description = data['description']
    )
    embed.add_field(name= 'Nation',value=data['nation'],inline=True)
    embed.add_field(name= 'Affiliation',value=data['affiliation'],inline=True)
    embed.add_field(name= 'Element Type',value=f"{data['vision']} {elementEmoji(data['vision'])}",inline=True)
    embed.add_field(name= 'Rarity',value= getRarity(data['rarity']),inline=True)
    embed.add_field(name= 'Constellation',value=data['constellation'],inline=True)
    embed.add_field(name= 'Weapon',value=data['weapon'],inline=True)
    embed.set_thumbnail(url = icon[temp])
    embed.set_image(url = 'https://i.imgur.com/AnAvjd3.png')
    data_info = discord.Embed.to_dict(embed)
    with open(f'{temp2}/introduction.json', 'w', encoding='utf-8') as f:
        json.dump(data_info, f, ensure_ascii=False, indent=4)