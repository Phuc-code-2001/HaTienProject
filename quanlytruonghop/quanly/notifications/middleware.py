from .models import UserChannel, PersonalNotification, GroupNotification


class CheckChannelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.user.is_authenticated and request.user.user_channel is None:
            UserChannel.objects.create(user=request.user)
        
        return response
    
# class NotificationMiddleware:
    
#     def __init__(self, get_response):
#         self.get_response = get_response
        
#     def __call__(self, request):
#         response = self.get_response(request)
        
#         return response
        
#     def process_template_response(self, request, response):
        
#         if request.user.is_authenticated:
#             query_set = list(PersonalNotification.objects.filter(receiver=request.user))
#             groups = request.user.groups
#             query_set += list(GroupNotification.objects.filter(group_receiver=groups.first()))
            
#             response.context_data["notification"] = [n.toJson() for n in query_set]
        
#         return response