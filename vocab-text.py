
#!/usr/bin/python3

import schedule
import time 

from wordnik import *
import json
import datetime
import urllib

from twilio.rest import Client

#Twillo
number = 777777777 #number to send texts to 
twilio_number = 8888888888 #Your Twillo number 
account = "Twillo-Account-ID"
token = "Twillo-API-Token"
client = Client(account,token)

#Wordnik
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'Wordnik-API-Key'

def send_message(quote):

	client.messages.create(to=number,from_=twilio_number,body=quote)
	print("Text sent!")

def compose_message():

	now=datetime.datetime.now()
	today=str(now.year)+'-'+str(now.month)+'-'+str(now.day)
	
	url = 'http://api.wordnik.com:80/v4/words.json/wordOfTheDay?date='+today+'&api_key='+apiKey


	with urllib.request.urlopen(url) as url:
	    s = url.read()

	    p = json.loads(s)

	    quote= "Word of the Day: "+p['word']+"\n"

	    for defe in p['definitions']:

	    	quote+=defe['text']+"\n"

	return quote 


def job():
	send_message(compose_message())


schedule.every().day.at("12:42").do(job)

while True:
	schedule.run_pending()
	time.sleep(1)

