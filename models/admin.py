# your_app/admin.py

from django.contrib import admin
from .models import UserModel, ChechingModel
from django.http import HttpResponse
from django.urls import path

class UserAdmin(admin.ModelAdmin):
    list_display = ['finger_id', 'full_name', 'status']
    list_filter = ['full_name', 'status']
    search_fields = ['full_name', 'finger_id', 'role']
    list_editable = ['status']
admin.site.register(UserModel, UserAdmin)

@admin.register(ChechingModel)
class CheckingAdmin(admin.ModelAdmin):
    list_display = ['user', 'checking_status', 'time']




# python manage.py runserver
# celery -A config worker --loglevel=info


