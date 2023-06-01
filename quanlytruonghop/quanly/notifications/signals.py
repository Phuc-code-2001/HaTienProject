from topicyeucau.models import Topic, MyTopic
from .models import GroupNotification, PersonalNotification

from django.contrib.auth.models import Group

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.urls import reverse

@receiver(post_save, sender=Topic)
def post_save_topic(sender, instance, created, **kwargs):
    
    if created:
        topic : Topic = instance
        GroupNotification.objects.create(
            group_receiver=Group.objects.filter(name='manageUser').first(),
            title='Có yêu cầu mới',
            content=f'Yêu cầu mới từ {topic.author.userprofile.name}',
            link=reverse('topic_detail', args=(topic.pk, )),
        )

@receiver(post_save, sender=MyTopic)
def post_assign_topic(sender, instance, created, **kwargs):
    
    assigned : MyTopic = instance
    if assigned.employee is not None:
        
        if assigned.status == 'Đang xử lý':
            
            PersonalNotification.objects.create(
                receiver=assigned.employee,
                title='Có yêu cầu chuyển đến',
                content=f'Bạn được giao phó yêu cầu đến từ {assigned.topic.author.userprofile.name}',
                link=reverse('topic_detail', args=(assigned.topic.pk, )),
            )
            
            PersonalNotification.objects.create(
                receiver=assigned.topic.author,
                title=f'Yêu cầu đang chờ xử lý',
                content=f'Yêu cầu {assigned.topic.pk} sẽ được xử lý bởi {assigned.employee.userprofile.name}',
                link=reverse('topic_detail', args=(assigned.topic.pk, )),
            )
            
        elif assigned.status == 'Hoàn thành':
            
            PersonalNotification.objects.create(
                receiver=assigned.topic.author,
                title=f'Yêu cầu đã xử lý xong',
                content=f'Yêu cầu {assigned.topic.pk} đã hoàn thành',
                link=reverse('topic_detail', args=(assigned.topic.pk, )),
            )
        
    