from rest_framework import serializers
from .models import Language
from django.contrib.auth.models import User

class LanguageSerializer(serializers.ModelSerializer):
    """ Serializer for languages. """

    class Meta:
        model = Language
        fields = ('name', 'about', 'image', 'level')

    
class RegisterSerializer(serializers.ModelSerializer):
    """ Serializer for user. """
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)