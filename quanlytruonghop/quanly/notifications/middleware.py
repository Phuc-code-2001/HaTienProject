from .models import UserChannel



class CheckChannelMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.user.is_authenticated and request.user.user_channel is None:
            UserChannel.objects.create(user=request.user)  
        
        return response