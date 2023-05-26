import setuptools

description = """
# Secret-Message 
[![PyPI](https://img.shields.io/pypi/v/secret-message?color=blueviolet&label=Web-version%20&logo=appveyor&style=plastic)](https://secret-msg.onrender.com/)

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/PurpleBird7613/secret_msg?color=inactive&label=GitHub)](https://github.com/PurpleBird7613/secret_msg)

[![PyPI](https://img.shields.io/pypi/v/secret-message?color=blue&label=python-package&style=plastic)](https://pypi.org/project/secret-message/)

Create and share Messages in a  **Secret** way.

## Install
```python
pip install secret-message
```

## Import the package
```python
import secret_message

# ------OR------

#from secret_message import create,show,history
```

## Create a Message:
```python
import secret_message as message 

message.create("<USERNAME>","<YOUR_MESSAGE>","<PASSWORD_FOR_THE_MESSAGE>")
```
For creating a message it takes only 3 parameters:
```
1. Username - Just add your name as username(No registration stuff is required.)
	
2. Text Message - You can add your message 
	
3. Message Password = Create a password of your choice for the message you are creating 
```

• Output:
```python
{
  "id": <YOUR_MESSAGE_ID>,
  "text_message": "<YOUR_MESSAGE>",
  "password": "<YOUR_MESSAGE_PASSWORD>",
  "web_msg_link": "<YOUR_MESSAGE_LINK_FOR_WEB>",
  "api_msg_link": "<YOUR_MESSAGE_LINK_FOR_API_CALL>"  
}
```
```
web_message_link - Using this link anyone will be able to access your message from web[Any web browser].

api_msg_link - Using this link anyone will be able to access your message by api call 
```

## Show/Read Message
```python
import secret_message as message

message.show("<USERNAME>","<MESSAGE_LINK>","<PASSWORD_OF_THE_MESSAGE>")
```
For showing or reading someone else's messages,it takes only 3 parameters:
```
1. Username - Just add your name as username(No registration stuff is required.)
	
2. Message Link - This link must the "api_msg_link" in order to read or view the message.
	
3. Password - This must be the exact password for the message created by other user.
```
	
• Output:
```python
{
  "text_message" : "<USER'S_MESSAGE>"
}
```

## Message History 
```python
import secret_message as message

message.history("<Username>")
```
For getting history of your messages,it takes only 1 parameter:
```
1. Username - Just add your name as username(No registration stuff is required.)
```

• Output:
```python
{
  "Messages": [
  	{
  	   "id": <YOUR_MESSAGE_ID>,
  	   "text_message": "<YOUR_MESSAGE>",
  	   "password": "<YOUR_MESSAGE_PASSWORD>",
  	   "web_msg_link": "<YOUR_MESSAGE_LINK_FOR_WEB>",
  	   "api_msg_link": "<YOUR_MESSAGE_LINK_FOR_API_CALL>" 
  	},
  	........,
  ]
}
```


"""          

setuptools.setup(

	name = 'secret_message', 

	version = '0.10',

	author = "E Lusifa Taehyung",

	author_email = "purplebird7613@gmail.com",

	description = "Create and share a Message Secretly.",
	
	long_description = description,
	
    long_description_content_type = 'text/markdown',
  
	
	packages = setuptools.find_packages(),
 
	classifiers = [

    "Programming Language :: Python",

    "License :: OSI Approved :: MIT License",

    "Operating System :: OS Independent",

    ],

) 