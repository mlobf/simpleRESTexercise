from rest_framework import generics, filters
from rest_framework.views import APIView

from core.models import Imovel, Imobiliaria
from core.api.serializers import ImovelSerializer, ImobiliariaSerializer
from django.http import JsonResponse, HttpResponse

"""
    Foi utilizado uma abstração de alto nivel
    do Django Rest Framework chamada generic.APIViews.
    
    => https://www.django-rest-framework.org/api-guide/generic-views/

    Esta possui metodos que representam das entidades as seguintes operações:

        -> Listagem.
        -> Criação.
        -> Detalhamento. 
        -> Atualização.
        -> Destruição.

"""


# --------------------------  Imovel    -------------------------------------#
class ImovelListAPIView(generics.ListAPIView):
    queryset = Imovel.objects.all().order_by("nome")
    serializer_class = ImovelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome"]


class ImovelCreateAPIView(generics.CreateAPIView):
    queryset = Imovel.objects.all().order_by("-id")
    serializer_class = ImovelSerializer


class ImovelDetailAPIView(generics.RetrieveAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer


class ImovelUpdateAPIView(generics.UpdateAPIView):
    queryset = Imovel.objects.all().order_by("-id")
    serializer_class = ImovelSerializer


class ImovelDestroyAPIView(generics.DestroyAPIView):
    queryset = Imovel.objects.all().order_by("-id")
    serializer_class = ImovelSerializer


# -------------------------  Imobiliaria    ---------------------------------#
class ImobiliariaListAPIView(generics.ListAPIView):
    queryset = Imobiliaria.objects.all().order_by("nome")
    serializer_class = ImobiliariaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome"]


class ImobiliariaCreateAPIView(generics.CreateAPIView):
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer


class ImobiliariaDetailAPIView(generics.RetrieveAPIView):
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer


class ImobiliariaUpdateAPIView(generics.UpdateAPIView):
    queryset = Imobiliaria.objects.all().order_by("-id")
    serializer_class = ImobiliariaSerializer


class ImobiliariaDestroyAPIView(generics.DestroyAPIView):
    queryset = Imobiliaria.objects.all().order_by("-id")
    serializer_class = ImobiliariaSerializer


# ----------------------------------------------------------------------------#
