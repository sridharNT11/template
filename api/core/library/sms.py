import requests, json
from core import app

class SMS():	
	# Eg single SMS: send('9952514049','this single test message')
	# EG one message to mutiple mobile number : send('9952514049,1231231231','this mutuple test message') 
	def send(self,mobile,message):
		url_sms = 'http://api.msg91.com/api/v2/sendsms'
		data = { 
				"sender": "NTECRG",
				"route": "4",
				"country": "91",
				"sms": [
							{
								"message": message,
								"to": [mobile]
							}
					   ]
		
		       }
		headers = { 
					'authkey': "231926AE3o5GFOkdM5c110b52", #MSG91 Numerotec account API Key
					'Content-Type': "application/json"
				  }

		response = requests.request("POST", url_sms, data=json.dumps(data),  headers=headers)
		return response.text

