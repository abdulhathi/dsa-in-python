
# ^ We need to install the requests library using 'pip3 install requests'
import requests

url = 'http://www.ibm.com'
response = requests.get(url)
print(response)

print(response.status_code)
"""
200
"""
print(response.headers)
"""
{'Content-Security-Policy': 'upgrade-insecure-requests', 'x-frame-options': 'SAMEORIGIN', 'Last-Modified': 'Mon, 01 Sep 2025 21:25:14 GMT', 'ETag': '"2e1cb-63dc401db96f8-gzip"', 'Accept-Ranges': 'bytes', 'Content-Type': 'text/html;charset=utf-8', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'max-age=600', 'Expires': 'Mon, 01 Sep 2025 21:41:05 GMT', 'X-Akamai-Transformed': '0 - 0 -', 'Content-Encoding': 'gzip', 'Date': 'Mon, 01 Sep 2025 21:31:05 GMT', 'Content-Length': '36989', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Strict-Transport-Security': 'max-age=31536000'}
"""
print(response.request.body)              #* None
print(response.headers['date'])           #* Mon, 01 Sep 2025 21:33:36 GMT
print(response.headers['Content-Type'])   #* text/html;charset=utf-8
print(response.encoding)                  #* utf-8
print(response.text[1:100])
"""
<!DOCTYPE HTML>
<html lang="en">
<head>
"""