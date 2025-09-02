import requests
import pandas as pd
import json

url_get = 'https://official-joke-api.appspot.com/jokes/ten'

response = requests.get(url_get)
jokes = json.loads(response.text)
df = pd.json_normalize(jokes)
df.drop(columns=['type','id'], inplace=True)
print(df)