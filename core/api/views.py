from rest_framework import generics, filters

from rest_framework.views import APIView

from core.models import Imovel, Imobiliaria, Endereco
from core.api.serializers import ImovelSerializer, ImobiliariaSerializer
from django.http import JsonResponse, HttpResponse

# ------------------      Imovel           -------------------------------------#
class ImovelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Imovel.objects.all().order_by("-id")
    serializer_class = ImovelSerializer
    # search_fields = ["nome"]
    # permission_classes = [IsAdminUserOrReadOnly]


class ImovelCreateAPIView(generics.CreateAPIView):
    queryset = Imovel.objects.all().order_by("-id")
    serializer_class = ImovelSerializer
    # search_fields = ["nome"]
    # permission_classes = [IsAdminUserOrReadOnly]


class ImovelDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    # search_fields = ["nome"]
    # permission_classes = [IsAdminUserOrReadOnly]


# -----------------------------------------------
class ImovelListAPIView(generics.ListAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome"]


# -------------------------  Imobiliaria    ------------------------------------#
class ImobiliariaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Imobiliaria.objects.all().order_by("-id")
    serializer_class = ImobiliariaSerializer
    search_fields = ["nome"]
    # permission_classes = [IsAdminUserOrReadOnly]


class ImobiliariaDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer
    search_fields = ["nome"]
    # permission_classes = [IsAdminUserOrReadOnly]


class ImobiliariaListAPIView(generics.ListAPIView):
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer
    filter_backends = [filters.SearchFilter]

    search_fields = ["nome"]


# ---------------------------------------------------------------------------#
