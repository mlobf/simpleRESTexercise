from rest_framework import generics
from core.models import Imovel, Imobiliaria
from core.api.serializers import ImovelSerializer, ImobiliariaSerializer


class ImovelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Imovel.objects.all().order_by("-id")
    serializer_class = ImovelSerializer
    # permission_classes = [IsAdminUserOrReadOnly]


class ImovelDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    # permission_classes = [IsAdminUserOrReadOnly]


class ImobiliariaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Imobiliaria.objects.all().order_by("-id")
    serializer_class = ImobiliariaSerializer
    # permission_classes = [IsAdminUserOrReadOnly]


class ImobiliariaDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer
    # permission_classes = [IsAdminUserOrReadOnly]
