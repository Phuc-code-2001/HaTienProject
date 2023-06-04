from django.core.mail import send_mail
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save

from notifications.models import GroupNotification, PersonalNotification, Notification
from django.contrib.auth.models import User, Group

EMAIL_SERVER = settings.EMAIL_HOST_USER

def send_notification(recipient_list_validated : list[User], subject, message):
    return send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_SERVER,
        recipient_list=recipient_list_validated,
    )

@receiver(post_save, sender=GroupNotification)
def send_to_group(sender, instance, created, **kwargs):
    
    if created:
        group = instance.group_receiver
        users = group.user_set.all()
        recipient_list = []
        for _receiver in users:
            if _receiver.email:
                recipient_list.append(_receiver.email)
            else:
                print(f"W: The user '{_receiver.userprofile.name}' do not have email to send notification!")
        
        if len(recipient_list) != 0:
            subject = instance.title
            message = instance.content
            send_notification(recipient_list, subject, message)
    

@receiver(post_save, sender=PersonalNotification)
def send_to_one(sender, instance, created, **kwargs):
    
    if created:
        _receiver = instance.receiver
        recipient_list = []
        if _receiver.email:
            recipient_list.append(_receiver.email)
        else:
            print(f"W: The user '{_receiver.userprofile.name}' do not have email to send notification!")
        
        if len(recipient_list) != 0:
            
            subject = instance.title
            message = instance.content
            
            if _receiver.groups.filter(name='Employee').count():
                message += f". Truy cập http://127.0.0.1:8000/n/view-notification/{instance.pk} để xem."
            
            send_notification(recipient_list, subject, message)
    