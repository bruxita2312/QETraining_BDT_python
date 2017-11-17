import requests
# sending requests
r= requests.get('https://api.github.com/events')
print("Values \n", r.text)
print ("CONTENT \n", r.content)
print ("CODE \n", r.status_code)


payload = {'key1': 'value1', 'key2':'value2'}
r = requests.post("https://api.github.com/events", data = payload)
print (r.text)


# adding headers
url = 'url_endpoint'
header = {'user-agent': 'my-app/0.0.1'}
r= requests.get(url,headers=headers)

#responses
response.content
response.json()
response.text
responst.status_code