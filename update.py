import json, os
artfs = json.load(open('artifacts.json', 'r'))
data = json.load(open('data.json', 'r'))

x2 = '<:2x:957694031343812619>'
x4 = '<:4x:957694032216215573>'

def format_guide(guides_dict: dict):
    for field in guides_dict['fields']:
        if 'Set' in field['name']:
            try:
                sets = field['value'].split('*')
                test = sets[1].replace(' ','').replace('\n',' ').replace('<','|').replace('>', '|').lower().split('|')
                print(test)
                description = ''

                
                field['value'] = description
            except:
                continue
    return guides_dict
    
# rootdir = '/Users/zaeem/Desktop/Character Guides/'
# for file in os.listdir(rootdir):
#     d = os.path.join(rootdir, file)
#     if os.path.isdir(d):
#         # path = d + '/build.json'
#         path = 'data.json'
#         embed_dict = json.load(open(path))
#         test = format_guide(embed_dict)
test = format_guide(data)