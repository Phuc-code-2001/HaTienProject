from django.db import models
from django.contrib.auth.models import User, Group

from secrets import token_hex

# Create your models here.
class Notification(models.Model):
    
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    read_at = models.DateTimeField(null=True, blank=True, default=None)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def toJson(self):
        return dict(
            id=self.pk,
            title=self.title,
            content=self.content,
            link=self.link,
            seen=self.read_at is not None,
            create_at=str(self.create_at)
        )
    

class PersonalNotification(Notification):
    receiver = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
class GroupNotification(Notification):
    group_receiver = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name='notifications')
    

def generate_secret():
    return token_hex(16)

class UserChannel(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_channel')
    channel = models.TextField(max_length=255, default=generate_secret)

