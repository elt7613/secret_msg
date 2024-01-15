import requests
import json
import os
import base64

host = "https://secretmessage.pythonanywhere.com"

# ====== Getting Token as User ======
def user(username):
	url = f"{host}/api/create-user/"
	
	data = {
			"name" : username
		}
	response = requests.post(url,data = data)
	
	obj = json.loads(response.text)
	
	return obj["Token"]

# ====== Creating Message ====== 
def create(username,msg,img,msg_pass):
	url = f"{host}/api/create-message/"
	
	print(f"Connecting {username}.....")
	User = user(username)
	
	headers = {
			"Authorization" : f"Token {User}"	
		}
	data = {
			"text_message" : msg,
			"password" : msg_pass
		}
	try:
		image = open(img,"rb")
		files = {
			"image" : image,
		}
	except:
		files = {
			"image" : img
		}
	
	print("Creating Message.....")	
	response = requests.post(url,headers = headers,data = data, files=files)
	
	obj = json.loads(response.text)
	print(json.dumps(obj,indent = 3,ensure_ascii = False))
	
	return obj	


# ===== Showing Message ======
def show(username,msg_url,msg_pass):
	url = msg_url
	
	print(f"Connecting {username}.....")
	User = user(username)
	
	headers = {
			"Authorization" : f"Token {User}"	
		}
	data = {
			"password" : msg_pass
		}
	
	print("Getting The Message......")	
	response = requests.post(url,headers = headers,data = data)
	
	obj = json.loads(response.text)
	print(json.dumps(obj["Message"],indent = 3,ensure_ascii = False))
	
	return obj

# ====== Message History ======
def history(username):
	url = f"{host}/api/message-history/"
	
	print(f"Connecting {username}.....")
	User = user(username)
	
	headers = {
			"Authorization" : f"Token {User}"	
		}
	
	print("Getting Message History.....")	
	response = requests.get(url,headers = headers)
	
	obj = json.loads(response.text)
	print(json.dumps(obj,indent = 3,ensure_ascii = False))
	
	return obj
	