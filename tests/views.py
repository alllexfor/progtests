from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import response, status
from .models import Language
from .serializers import LanguageSerializer, RegisterSerializer
from django.middleware import csrf
from rest_framework.decorators import api_view


# Create your views here.
class Languages(ListAPIView):
    """ Api for all languages and frameworks. """

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


@api_view()
def get_csrf_token(request):
    """ Api for csrf token. """

    token = csrf.get_token(request)
    return response.Response({'token': token})


class RegisterApi(GenericAPIView):
    """ Api for user registration. """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)
        return response.Response(serializer.data,
                                 status=status.HTTP_400_BAD_REQUEST)
