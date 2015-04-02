from django.contrib import admin

# Register your models here.
from photo.models import HashTag, Photo, Comment

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('by', 'on', 'description')

admin.site.register(HashTag)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment)