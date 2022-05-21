from rest_framework import serializers
from .models import Language
from django.contrib.auth.models import User


class LanguageSerializer(serializers.ModelSerializer):
    """ Serializer for languages. """

    class Meta:
        model = Language
        fields = ('name', 'about', 'image', 'level')
