from django.urls import path
from core.api.views import (
    ImovelListAPIView,
    ImovelCreateAPIView,
    ImovelDetailAPIView,
    ImovelUpdateAPIView,
    ImovelDestroyAPIView,

    ImobiliariaCreateAPIView,
    ImobiliariaListAPIView,
    ImobiliariaDetailAPIView,
    ImobiliariaUpdateAPIView,
    ImobiliariaDestroyAPIView,
)

urlpatterns = [
    # IMOVEIS------------------------------------------------------------------------------------#
    path("imovel/", ImovelListAPIView.as_view(), name="imovel-list"),
    path("imovel/create", ImovelCreateAPIView.as_view(), name="imovel-create"),
    path("imovel/detail/<int:pk>/", ImovelDetailAPIView.as_view(), name="imovel-detail"),
    path("imovel/update/<int:pk>/", ImovelUpdateAPIView.as_view(), name="imovel-update"),
    path("imovel/delete/<int:pk>/", ImovelDestroyAPIView.as_view(), name="imovel-delete"),
    # IMOBILIARIA---------------------------------------------------------------------------------#

    path("imobiliaria/", ImobiliariaListAPIView.as_view(), name="imobiliaria-list"),
    path("imobiliaria/create", ImobiliariaCreateAPIView.as_view(),name="imobiliaria-create"),
    path("imobiliaria/detail/<int:pk>/", ImobiliariaDetailAPIView.as_view(), name="imobiliaria-detail"),
    path("imobiliaria/update/<int:pk>/", ImobiliariaUpdateAPIView.as_view(), name="imobiliaria-update"),
    path("imobiliaria/delete/<int:pk>/", ImobiliariaDestroyAPIView.as_view(), name="imobiliaria-delete"),
    # --------------------------------------------------------------------------------------------#
]
