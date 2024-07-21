import os
import sys
import json
import logging
import requests
import discord

from git import Repo

# DOWNLOAD CHUNK SIZE
CHUNK_SIZE = 5 * 2**20
RETRY_MAX = 10

LOGGER = logging.getLogger(__name__)

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if GITHUB_TOKEN:
    HEADER["Authorization"] = f"token {GITHUB_TOKEN}"

def elementColor(element):
    return {
        'Dendro':6794623, 
        'Hydro':3245055, 
        'Anemo':5494962, 
        'Geo':14994176, 
        'Pyro':16733525, 
        'Cryo':10147839, 
        'Electro':11104511
    }.get(str(element))
    
def getBanner(element):
    return {
        'Dendro':'http://cdn.genshinwizard.com/4/08768dec91/dendro.png', 
        'Hydro':'http://cdn.genshinwizard.com/2/047417908b/hydro.png', 
        'Anemo':'http://cdn.genshinwizard.com/7/02a10edbdb/anemo.png', 
        'Geo':'http://cdn.genshinwizard.com/7/07a6839a95/geo.png', 
        'Pyro':'http://cdn.genshinwizard.com/4/0a3c3868af/pyro.png', 
        'Cryo':'http://cdn.genshinwizard.com/2/01834bf617/cryo.png', 
        'Electro':'http://cdn.genshinwizard.com/4/0930c70f80/electro.png'
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

def weaponType(weaponType):
    return {
        "WEAPON_CATALYST":"<:Skill_A_Catalyst_MD:1063905220104556694> Catalyst", 
        "WEAPON_BOW":"<:Skill_A_02:1063905222927331369> Bow", 
        "WEAPON_CLAYMORE":"<:Skill_A_04:1063905227050328094> Claymore", 
        "WEAPON_SWORD":"<:Skill_A_01:1063905221815832738> Sword", 
        "WEAPON_POLEARM":"<:Skill_A_03:1063905224651190462> Polearm"
    }.get(str(weaponType))

character_id = sys.argv[1]
if not character_id:
    print("[ERROR] No character ID provided. [Usage: py generate_character.py <character_id>")
    sys.exit(1)

if os.path.exists(character_id):
    print(f"[ERROR] {character_id} guide already exists.")
    sys.exit(1)

os.makedirs(character_id, exist_ok=True)

ambr_url = f"https://api.ambr.top/v2/en/avatar/{character_id}"

CHARACTER_DATA = requests.get(ambr_url).json()
CHARACTER_DATA = CHARACTER_DATA['data']
character = CHARACTER_DATA['name']

element = {
    "Grass":"Dendro",
    "Ice":"Cryo",
    "Fire":"Pyro",
    "Wind":"Anemo",
    "Rock":"Geo",
    "Water":"Hydro",
    "Electric":"Electro",
}.get(CHARACTER_DATA['element'], "Unknown")

character_image = f"https://api.ambr.top/assets/UI/{CHARACTER_DATA['icon']}.png"

""" SYNERGY EMBED """
embed = discord.Embed(
    title = f'{character} | Team Composition and Synergy',
    color = elementColor(element),
    description = f"{CHARACTER_DATA['id']}"
)
embed.set_thumbnail(url = character_image)
embed.set_footer(text=f'Character Guide • Synergy: {character}')
synergy_json = discord.Embed.to_dict(embed)

""" PLAYSTYLE EMBED """
embed = discord.Embed(
    title = f'{character} | Playstyle',
    color = elementColor(element),
    description = "Unknown"
)
embed.set_thumbnail(url = character_image)
embed.set_footer(text=f'Character Guide • Playstyle: {character}')
playstyle_json = discord.Embed.to_dict(embed)

""" BUILDS EMBED """
embed = discord.Embed(
    title = f'{character} (Speculation Build) | Build',
    color = elementColor(element),
)
embed.add_field(
    name = "Best Weapon(s):",
    value = "Unknown",
    inline = True
)
embed.add_field(
    name = "Replacement Weapon(s):",
    value = "Unknown",
    inline = True
)
embed.add_field(
    name = "Best Artifact Set:",
    value = "Unknown",
    inline = False
)
embed.add_field(
    name = "Second Best Artifact Set:",
    value = "Unknown",
    inline = False
)
embed.add_field(
    name = "Third Best Artifact Set:",
    value = "Unknown",
    inline = False
)
embed.add_field(
    name = "Main Stats Priority",
    value = "<sands> Unknown|<goblet> Unknown|<circlet> Unknown",
    inline = True
)
embed.add_field(
    name = "Substats Priority",
    value = "Unknown|Unknown|Unknown",
    inline = True
)
embed.add_field(
    name = "Talent Priority",
    value = "**1)** Unknown\n**2)** Unknown\n**3)** Unknown",
    inline = False
)
embed.set_thumbnail(url = character_image)
embed.set_footer(text=f'Character Guide • Build: {character}')
builds_json = [discord.Embed.to_dict(embed)]

file_types = ["synergies", "playstyle", "builds"]
files = [synergy_json, playstyle_json, builds_json]
for file in files:
    with open(f'{CHARACTER_DATA["id"]}/{file_types[files.index(file)]}.json', 'w') as f:
        json.dump(file, f, indent=4)

repo = Repo.init()
repo.index.add([
    f"{character_id}/synergies.json", 
    f"{character_id}/playstyle.json", 
    f"{character_id}/builds.json"
])
repo.index.commit(f"[Guide Creation] {character_id} Guide")
origin = repo.remote(name="origin")
origin.fetch()
origin.push()