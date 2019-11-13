#! python3
# twilio_demo.py - An introduction to using the twilio API to send SMS
# https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236

from twilio.rest import Client
import requests

# I couldn't get the os module to read my environment variables, so I'm placing
# dummy values here for now
account_sid = '********'
auth_token = '********'

client = Client(account_sid, auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

numberIss = people['number']

Message = 'No, you\'re the best & the prettiest.'

# Formulate the message that will be sent
message = client.messages.create(
	to='aPhoneNumber',
	from_='aPhoneNumber',
	body=Message)

print(message.sid)