from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .models import Language
from .serializers import LanguageSerializer
from rest_framework.permissions import IsAuthenticated


class Languages(ListAPIView):
    """ Api for all languages and frameworks. """

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
