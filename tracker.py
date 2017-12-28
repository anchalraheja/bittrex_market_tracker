import requests
import json
import urllib3
import urllib2
import winsound
from playsound import playsound
import time


print ('*'* 150)

for x in xrange(1,1000):
	pass
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	http = urllib3.PoolManager()
	r = http.request('GET',"https://bittrex.com/api/v1.1/public/getticker?market=btc-ltc")
	json_data = json.loads(r.data.decode('UTF-8'))
	last = json_data['result']['Last']
	if last > 0.01711000:
		print last
		print time.strftime("%Y-%m-%d %H:%M:%S")
		playsound('2.mp3')


