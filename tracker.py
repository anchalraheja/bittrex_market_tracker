import requests
import json
import urllib3
import urllib2


print ('*'* 150)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()
r = http.request('GET',"https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc")
json_data = json.loads(r.data.decode('UTF-8'))
#print (json_data)
# print ('*'* 150)
# #print ('message',json_data['Low'])

# # print ('items', json_data.items())
# print ('+'* 150)


# print ('keys', json_data.keys())
# print ('+'* 150)



# print ('values', json_data.values())
# print ('+'* 150)

print (json_data['result'][0]['High'])
