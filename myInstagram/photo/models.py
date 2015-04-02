from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HashTag(models.Model):
	name = models.CharField(max_length = 100)
	photo_count = models.IntegerField(default = 0)
	def __str__(self):
		return '#' + self.name

class Photo(models.Model):
	photo = models.ImageField(upload_to='uploads/')
	by = models.ForeignKey(User, related_name = 'photos')
	on = models.DateTimeField(auto_now_add = True)
	description = models.TextField(max_length = 300, null = True)
	user_tags = models.ManyToManyField(User, related_name = 'tagged_in')
	likers = models.ManyToManyField(User, related_name = 'liked')
	has_tags = models.ManyToManyField(HashTag)

	def __str__(self):
		return 'By: ' + self.by.first_name
	
class Comment(models.Model):
	by = models.ForeignKey(User)
	photo = models.ForeignKey(Photo)
	on = models.DateTimeField(auto_now_add = True)
	text = models.CharField(max_length = 1000)

	def __str__(self):
		return self.text
