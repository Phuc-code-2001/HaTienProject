from django.urls import path

from .views import get_list_notifications, remove_notification, view_notification

urlpatterns = [
    path('get-list-notification/', get_list_notifications, name='get-list-notification'),
    path('remove-notification/<int:id>', remove_notification, name='remove-notification'),
    path('view-notification/<int:id>', view_notification, name='view-notification'),
]