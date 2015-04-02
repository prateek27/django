from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# from account.models import City, State, Country, UserProfile
from .models import *

class UserInLine(admin.StackedInline):
	model = UserProfile
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (UserInLine, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(UserProfile)
