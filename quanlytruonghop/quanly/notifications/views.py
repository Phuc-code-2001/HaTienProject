from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import PersonalNotification, GroupNotification

# Create your views here.
def get_list_notifications(request):
    
    if request.user.is_authenticated:
        n_personal = PersonalNotification.objects.filter(receiver=request.user).order_by('-create_at')[:5]
        n_grouped = GroupNotification.objects.filter(group_receiver=request.user.groups.first()).order_by('-create_at')[:5]
        converted_data = [item.toJson() for item in n_personal] + [item.toJson() for item in n_grouped]
        converted_data.sort(key=lambda x: x.get('create_at'))
        
        return JsonResponse(data=converted_data, safe=False)
    
    return HttpResponse(status=403)