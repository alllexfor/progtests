from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .models import Language
from .serializers import LanguageSerializer

# Create your views here.
class Languages(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer