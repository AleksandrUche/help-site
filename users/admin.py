from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    list_display = ['username', 'first_name', 'last_name', 'email']
    model = CustomUser

