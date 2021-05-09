from django.urls import path
from core.api.views import (
    ImovelDetailAPIview,
    ImovelListCreateAPIView,
    ImovelListAPIView,
    ImovelCreateAPIView,
    ImovelDestroyAPIView,
    ImovelUpdateAPIView,
    ImobiliariaDetailAPIview,
    ImobiliariaListCreateAPIView,
    ImobiliariaListAPIView,
)

urlpatterns = [
    # -------------------------------------------------------------------------------------------------#
    path("imovel/<int:pk>/", ImovelDetailAPIview.as_view(), name="imovel-detail"),
    path("imovel/<int:pk>/", ImovelDestroyAPIView.as_view(), name="imovel-delete"),
    path("imovel/<int:pk>/", ImovelUpdateAPIView.as_view(), name="imovel-update"),
    path("imovel/create", ImovelCreateAPIView.as_view(), name="imovel-create"),
    path("imovel/", ImovelListAPIView.as_view(), name="imovel-list"),


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
