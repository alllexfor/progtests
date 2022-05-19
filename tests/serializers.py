from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    """ API """

    class Meta:
        model = Language
        fields = ('name', 'about', 'image', 'level')