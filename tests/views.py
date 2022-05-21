from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

from .services import *


class Languages(ListAPIView):
    """ Api for all languages and frameworks. """

    queryset = get_all_objects(Language)
    serializer_class = LanguageSerializer


class LanguagesChoices(Languages):
    """ Api for user choices: level and type """

    def get_queryset(self):
        user_date = self.request.query_params
        return Language.objects.filter(level=user_date['level'], type_of=user_date['type_of'])