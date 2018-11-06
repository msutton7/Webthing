from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	# add additional fields in here
	#age = AbstractUser.PositiveIntegerField(_("age"), null=True)
	#age = 21
	age = IntegerField(default=170)

	#def __init__(self, score1=0, score2=0):
	#	self.score1 = score1
	#	self.score2 = score2

	def __str__(self):
		return self.email
		
#	def test(self):
#		return age

#class test(CustomUser):
#
#	def __str__(self):
#		return CustomUser.age