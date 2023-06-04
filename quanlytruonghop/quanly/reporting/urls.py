from django.urls import path
from .views import (
    index, 
    employee_ranking, 
    get_employee_report, 
    get_member_ranking,
    get_rating_on_month,
    get_rating_on_year,
)
urlpatterns = [
    path('overview/', index),
    path('employee-ranking/', employee_ranking),
    path('employee-report/', get_employee_report),
    path('member-ranking/', get_member_ranking),
    path('rating-on-month/', get_rating_on_month),
    path('rating-on-year/', get_rating_on_year),
]