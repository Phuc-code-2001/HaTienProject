from django.urls import path

from .views import get_list_notifications

urlpatterns = [
    path('get-list-notification/', get_list_notifications, name='get-list-notification')
]