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
                test = sets[1].replace('\n','').replace(' ','').replace('-','').replace("'",'').replace('\n',' ').replace('<','|').replace('>', '|').lower().split('|')
                
                if '2x' in test[1]:
                    description = f'x2-{test[0]}|x2-{test[2]}'
                else:
                    description = f'x4-{test[0]}'

                field['value'] = description
            except:
                continue
    return guides_dict
    
rootdir = '/Users/zaeem/Desktop/Character Guides/'
for file in os.listdir(rootdir):
    if file == '.git':
        continue
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        path = d + '/build.json'
        embed_dict = json.load(open(path))
        data = format_guide(embed_dict)
        with open(f'{file}/build.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)