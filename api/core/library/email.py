import requests, json
from core import app

class email():	
	def send(self,otp1):
		domain = "numerotec.com"
		api_key = "key-001c5299e254f6f646c3d3d0d43b87bb"

		result = requests.post(
		    "https://api.mailgun.net/v3/"+domain+"/messages",
		    auth = (
		        "api", api_key
		        ),
		    # files=[("attachment", ("test.jpg", open("files/test.jpg","rb").read())),        
		    #       ("attachment", ("test.txt", open("files/test.txt","rb").read()))],
		    data = {
		            "from": "tamilselvi@numerotec.com",
		            "to": "tamilselvi@numerotec.com",
		            #"cc": "keerthi@numerotec.com,meena@numerotec.com,tamilselvi@numerotec.com",
		            #"bcc": "ganesan@numerotec.com",
		            "subject": "Hello Python Test Mail",
		            "text": "Testing some Mailgun awesomness!",
		            "html": "<html>your otp:"+otp1+"</html>" 
		    }
		)
		print(result)
		return "Email was sent successfully"

		
		








	    