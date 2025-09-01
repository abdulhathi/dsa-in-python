import requests

url_get = 'https://httpbin.org/get'
payload = {"name": "Abdul", "ID": "123"}
response = requests.get(url_get, params=payload)

print(response.url) 
#* https://httpbin.org/get?name=Abdul&ID=123

print(response.request.body) #* None
print(response.status_code)

print(response.text)
print(response.headers['Content-Type'])
# ^ application/json
print(response.json())
# ^ {'args': {'ID': '123', 'name': 'Abdul'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.5', 'X-Amzn-Trace-Id': 'Root=1-68b61385-72f772c750d8d7a1277feaf2'}, 'origin': '136.52.18.164', 'url': 'https://httpbin.org/get?name=Abdul&ID=123'}

print(response.json()['args'])
# ^ {'ID': '123', 'name': 'Abdul'}