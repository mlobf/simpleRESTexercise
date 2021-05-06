from django.urls import path
from core.api.views import (
    ImovelDetailAPIview,
    ImovelListCreateAPIView,
    ImobiliariaDetailAPIview,
    ImobiliariaListCreateAPIView,
)

urlpatterns = [
    path("imovel/<int:pk>/", ImovelDetailAPIview.as_view(), name="imovel-detail"),
    path("imovel/", ImovelListCreateAPIView.as_view(), name="imovel-list"),

    path("imobiliaria/<int:pk>/", ImobiliariaDetailAPIview.as_view(), name="imobiliaria-detail"),
    path("imobiliaria/", ImobiliariaListCreateAPIView.as_view(), name="imobiliaria-list"),
]
