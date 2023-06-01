from django.contrib import admin

from .models import PersonalNotification, GroupNotification, UserChannel

# Register your models here.
@admin.register(PersonalNotification)
class PersonalNotificationAdmin(admin.ModelAdmin):
    
    list_display = ['receiver', 'title', 'create_at', 'read_at']
    
@admin.register(GroupNotification)
class GroupNotification(admin.ModelAdmin):
    
    list_display = ['group_receiver', 'title', 'create_at', 'read_at']
    
@admin.register(UserChannel)
class UserChannelAdmin(admin.ModelAdmin):
    
    list_display = ['user', 'channel']