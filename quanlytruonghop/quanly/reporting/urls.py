from django.urls import path
from .views import index, employee_ranking, get_employee_report, get_member_ranking

urlpatterns = [
    path('overview/', index),
    path('employee-ranking/', employee_ranking),
    path('employee-report/', get_employee_report),
    path('member-ranking/', get_member_ranking),
]