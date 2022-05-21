from django.urls import path
from .views import Languages

urlpatterns = [
    path('langauges/', Languages.as_view()),
]