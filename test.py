import requests
import json

api_key = '36a0c1c1f8abf0d9bbfe9dbab5edc06d'

file = open("odds.json", "w")

url = f'https://api.the-odds-api.com/v3/sports/?apiKey={api_key}'
odds_url = f'https://api.the-odds-api.com/v3/odds/?apiKey={api_key}&sport=basketball_nba&region=us&mkt=h2h'

response = requests.get(odds_url)

json.dump(response.json(), file)
file.close()