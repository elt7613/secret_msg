# Secret-Message 
[![PyPI](https://img.shields.io/pypi/v/secret-message?color=blue&style=plastic)](https://pypi.org/project/secret-message/)

Create and share Messages in a  **Secret** way.

## Install
```python
pip install secretmessage
```

## Import the package
```python
import secretmessage

# ------OR------

#from secretmessage import create,show,history
```

## Create a Message:
```python
import secretmessage as message 

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
import secretmessage as message

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
import secretmessage as message

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
