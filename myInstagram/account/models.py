from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length = 30, unique = True)
	class Meta:
		db_table = 'country'
		verbose_name_plural = 'Countries'
	def __str__(self):
		return self.name

class State(models.Model):
	country = models.ForeignKey(Country)
	name = models.CharField(max_length = 50)
	class Meta:
		db_table = 'state'
	def __str__(self):
		return self.country.name + '>' + self.name

class City(models.Model):
	state = models.ForeignKey(State)
	name = models.CharField(max_length = 70)
	class Meta:
		db_table= 'city'
		verbose_name_plural = 'cities'
	def __str__(self):
		return self.state.country.name + '>' + self.state.name + '>' + self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
	phone_number = models.CharField(max_length = 10, unique = True)
	city = models.ForeignKey(City)
	following_user = models.ManyToManyField("self", through = "Following", symmetrical = False, related_name = 'followers')
	class Meta:
		db_table = 'profile'
	def __str__(self):
		return self.user.username

class Following(models.Model):
	by = models.ForeignKey(UserProfile, related_name = 'follower')
	to = models.ForeignKey(UserProfile, related_name = 'followee')
	date_of_following = models.DateTimeField(auto_now_add = True)

