import requests
import json
import pandas as pd

url_get = "https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all"

data = requests.get(url_get)

results = data.json()
print(results)

df = pd.json_normalize(results)
print(df)

cherry = df.loc[df['name'] == 'Cherry']
print(cherry)

banana = df.loc[df['name'] == 'Banana']
print(banana['nutritions.calories'])
# banana.to_csv('00-basics/python/python-api/banana.csv')