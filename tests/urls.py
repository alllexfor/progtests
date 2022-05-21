from django.urls import path
from .views import RegisterApi, get_csrf_token, Languages

urlpatterns = [
    path('langauges/', Languages.as_view()),
    path('user/registration/', RegisterApi.as_view()),
    path('csrf/get_token/', get_csrf_token),
]