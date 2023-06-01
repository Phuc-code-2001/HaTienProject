from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Notification(models.Model):
    
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    read_at = models.DateTimeField(null=True, blank=True, default=None)
    create_at = models.DateTimeField(auto_now_add=True)
    

class PersonalNotification(Notification):
    receiver = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
class GroupNotification(Notification):
    group_receiver = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)