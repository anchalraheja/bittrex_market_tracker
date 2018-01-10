import requests
import json
import urllib3
import urllib2
import winsound
from playsound import playsound
import time

coin = raw_input("COIN NAME? ")
print coin

less_val= raw_input("Less Than Value ?")
print less_val
print ('*'* 150)
i = 1
while i < 5:
	print time.strftime("%S")
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	http = urllib3.PoolManager()
	r = http.request('GET',"https://bittrex.com/api/v1.1/public/getticker?market=btc-"+coin)
	json_data = json.loads(r.data.decode('UTF-8'))
	last = json_data['result']['Last']
	print last
	if last < less_val:
		print last
		print time.strftime("%Y-%m-%d %H:%M:%S")
		playsound('2.mp3')
		i = 6





