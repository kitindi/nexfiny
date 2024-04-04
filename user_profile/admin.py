from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Profile)

# mix profile and user info

class ProfileInline(admin.StackedInline):
    model = Profile
    
# extend user model

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username','first_name','last_name','email',]
    inlines = [ProfileInline]
    
# unregister the old ways
admin.site.unregister(User)

# register the new ways
admin.site.register(User, UserAdmin)