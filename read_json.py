import json

file = open('odds.json',)

data = json.load(file)

for i in data['data']:

    home_team = i['home_team']
    print('JOGO')
    print('-----------------------------------------')
    print(i['teams'])
    print(f'Home Team: {home_team}')
    print('-----------------------------------------')
    
    for j in i['sites']:
        
        print('ODDS')
        print('-----------------------------------------')
        site_name = j['site_nice']
        print(f'Site: {site_name}')
        print(j['odds'])
        print('-----------------------------------------')

file.close()