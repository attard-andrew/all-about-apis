#! python3
# datamuse.py - A sample in using the Datamuse API
# https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236

import requests

parameter = {'rel_rhy':'jingle'}
request = requests.get('https://api.datamuse.com/words', parameter)

rhyme_json = request.json()
for i in rhyme_json[0:3]:
	print(i['word'])