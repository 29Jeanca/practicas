from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView
from accounts.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/register/",RegisterView.as_view()),
    path("api/login/",LoginView.as_view()),
]
