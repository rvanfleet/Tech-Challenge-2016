import urllib2
import json

url = 'http://127.0.0.1:5000/createOrder'

parameters = {'partNumber': '123456'}

data = json.dumps(parameters)

req = urllib2.Request(url, data)

req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req)

print(response.read())
