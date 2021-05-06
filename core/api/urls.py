from django.urls import path
from core.api.views import (
    ImovelDetailAPIview,
    ImovelListCreateAPIView,
    ImovelListAPIView,
    ImobiliariaDetailAPIview,
    ImobiliariaListCreateAPIView,
    ImobiliariaListAPIView,
)

urlpatterns = [
    # -------------------------------------------------------------------------------------------------#
    path("imovel/<int:pk>/", ImovelDetailAPIview.as_view(), name="imovel-detail"),
    path("imovel/", ImovelListCreateAPIView.as_view(), name="imovel-list"),
    path("imovel/search", ImovelListAPIView.as_view(), name="imovel-search"),
    # -------------------------------------------------------------------------------------------------#
    path(
        "imobiliaria/<int:pk>/",
        ImobiliariaDetailAPIview.as_view(),
        name="imobiliaria-detail",
    ),
    path(
        "imobiliaria/", ImobiliariaListCreateAPIView.as_view(), name="imobiliaria-list"
    ),
    path(
        "imobiliaria/search",
        ImobiliariaListAPIView.as_view(),
        name="imobiliaria-search",
    ),
    # -------------------------------------------------------------------------------------------------#
]
