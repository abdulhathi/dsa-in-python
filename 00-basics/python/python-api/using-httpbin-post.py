import requests

url_post = 'http://httpbin.org/post'
payload = {'name': 'Abdul', 'id': "123"}

response = requests.post(url_post, data=payload)

print(response.request.url)
# ^ http://httpbin.org/post

print(response.json())
# ^ {'args': {}, 'data': '', 'files': {}, 'form': {'id': '123', 'name': 'Abdul'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '17', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.5', 'X-Amzn-Trace-Id': 'Root=1-68b61496-1b27d6ed62976d5f4ea72d63'}, 'json': None, 'origin': '136.52.18.164', 'url': 'http://httpbin.org/post'}

print(response.json()['form'])

# ^ {'id': '123', 'name': 'Abdul'}