from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser
from .forms import RegisterForm


admin.site.register(CustomUser)