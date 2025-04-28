from django.urls import path
from apps.user.views import get_users_list

urlpatterns = [
    path('', get_users_list),
]
