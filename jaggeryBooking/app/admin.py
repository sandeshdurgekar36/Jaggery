from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomUser)
class User(admin.ModelAdmin):
    list_display = ['id', 'username','mobile_number', 'email', 'full_name', 'address']

@admin.register(AvailableSlots)
class AvailableSlots(admin.ModelAdmin):
    list_display = ['id', 'slots_date_time']

@admin.register(UsersBookedSlots)
class UsersBookedSlots(admin.ModelAdmin):
    list_display = ['user_id',  'user','slot_date_time']

    def user(self, obj):
        return obj.user.full_name 

    def slot_date_time(self, obj):
        return obj.slots.slots_date_time 