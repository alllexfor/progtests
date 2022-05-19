from django.urls import path
from .views import Languages

urlpatterns = [
    path('', Languages.as_view()),
]