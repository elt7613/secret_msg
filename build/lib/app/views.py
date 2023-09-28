from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from .models import GitHub

import secret_message as message 
import json
	
# Logging in the Users
def signin(request):
	context ={}
		
	user = request.user
	context["user"] = user

	if user.is_authenticated:
		return redirect("home")
	
	github = GitHub.objects.all().order_by("-date")[0:1]
	context["github"] = github
	
	if request.method == "POST":
		username = request.POST.get('username','')
		login_user = authenticate(username=username, password="Password@")
		
		if login_user is not None:
			login(request,login_user)
			return redirect("home")
		else:
			user = User.objects.create_user(username, password="Password@")
			user.save()
			login(request,user)
			return redirect("home")
	
	return render(request,"login.html",context)

# Home
def home(request):
	context = {}
	
	user = request.user
	context["user"] = user
	
	if not user.is_authenticated:
		return redirect("/")
		
	github = GitHub.objects.all().order_by("-date")[0:1]
	context["github"] = github
	
	#------ HISTORY -------
	try:
		history = message.history(user)
		context["history"] = history["Messages"]
	except:
		pass
	
	#-------- Creating Message -------
	if request.method == "POST":
		msg = request.POST.get("message","")
		img = request.FILES["image"]
		password = request.POST.get("password","")
		print(msg,img,password)
		
		try:
			message.create(user,msg,img,password)
		except:
			message.create(user,msg,None,password)
		return redirect("home")
		
	return render(request,"home.html",context)