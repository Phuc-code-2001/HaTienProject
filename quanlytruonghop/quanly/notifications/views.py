from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse

from .models import PersonalNotification, GroupNotification, Notification
from django.contrib.auth.models import Group

import datetime

# Create your views here.
def get_list_notifications(request):
    
    if request.user.is_authenticated:
        n_personal = PersonalNotification.objects.filter(receiver=request.user).order_by('-read_at', '-create_at')[:10]
        n_grouped = GroupNotification.objects.filter(group_receiver=request.user.groups.first()).order_by('-read_at', '-create_at')[:10]
        converted_data = [item.toJson() for item in n_personal] + [item.toJson() for item in n_grouped]
        converted_data.sort(key=lambda x: x.get('create_at'))
        
        return JsonResponse(data=converted_data, safe=False)
    
    return HttpResponse(status=403)

def remove_notification(request, id):
    
    obj = get_object_or_404(Notification, pk=id)
    if obj:
        obj.delete()
        
    return HttpResponse(status=200)

def view_notification(request, id):
    
    common = get_object_or_404(Notification, pk=id)

    obj = PersonalNotification.objects.filter(id=id).first()
    if obj:
        if obj.receiver.groups.filter(name='Employee').count() and not obj.read_at:
            
            GroupNotification.objects.create(
                group_receiver=Group.objects.get(name="manageUser"),
                title=f"Ai đó đã truy cập tới yêu cầu cần xử lý",
                content=f"{obj.receiver.userprofile.name} đã truy cập tới yêu cầu cần xử lý",
                link=obj.link,
            )
        
    common.read_at = datetime.datetime.now()
    common.save()
    
    return redirect(common.link)