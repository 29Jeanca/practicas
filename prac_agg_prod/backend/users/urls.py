from django.urls import path
from .views import GetAllUsers, LoginAccount, RegisterAccount

urlpatterns = [
    path('register/', RegisterAccount.as_view(), name='register_account'),
    path('login/',LoginAccount.as_view(), name='login_account'),
    path('allUsers/',GetAllUsers.as_view(), name='all_users'),
]