import requests
import json

# get a free key on https://the-odds-api.com/


api_key = 'enter_your_free_key'

file = open("odds.json", "w")

url = f'https://api.the-odds-api.com/v3/sports/?apiKey={api_key}'
odds_url = f'https://api.the-odds-api.com/v3/odds/?apiKey={api_key}&sport=basketball_nba&region=us&mkt=h2h'

response = requests.get(odds_url)

json.dump(response.json(), file)
file.close()