from django.db import models

# App GitHub Link
class GitHub(models.Model):
	link = models.TextField(null = True,blank = True)
	date = models.DateTimeField(auto_now_add = True)