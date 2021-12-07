from .models.MyUser import MyUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'country', 'avatar')

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'country', 'avatar')


# Register your models here.
admin.site.register(MyUser, UserAdmin)