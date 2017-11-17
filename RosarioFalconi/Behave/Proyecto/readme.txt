features
	Scenarios
	Scenarios outline
steps
	*.py
		Actions
		Assertions > > compare library
environment.py >> hooks

config.yml


e.g.
behave -f plain --tags @any --summary --no-capture

AND >> scenario debe contener ambos tags
behave -f plain --tags @any --tags @some --summary --no-capture

OR
behave -f plain --tags @any,@some --summary --no-capture

NOT >> cuando hay un bug q no se fixeara
behave -f plain --tags @any --tags ~@some --summary --no-capture

pip install requests


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


jsondiff >> compara 2 json e indica sus diferencias

json.loads >>> correcto

jsonschema >> valida el schema


