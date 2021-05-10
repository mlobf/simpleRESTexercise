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
"""
    Neste arquivo é configurado os endpoints do programa.
    O Django usa um padrao ja pre estabelecido para padronizar
    a administraçao de urls.
    Ele precisa de todas as Views importadas para que estas
    venham a ser usadas em seus paths.
    
    => https://docs.djangoproject.com/en/2.2/topics/http/urls/ 

    A estrutura basica possui tres partes principais.
        1-  URL - estrutura do caminho a ser apresentado no navegador.
        2-  VIEW - a respectiva visualização a ser usada neste endpoint.
        3-  NAME - o nome que descreve a acao a ser executada no endpoint,
                    este deve refletir o caminho apresentado na url.
    
"""

urlpatterns = [
    # Estabelece os end-points para a Tabela IMOVEIS ----------------------------------------------#
    path("imovel/", ImovelListAPIView.as_view(), name="imovel-list"),
    path("imovel/create", ImovelCreateAPIView.as_view(), name="imovel-create"),
    path("imovel/detail/<int:pk>/", ImovelDetailAPIView.as_view(), name="imovel-detail"),
    path("imovel/update/<int:pk>/", ImovelUpdateAPIView.as_view(), name="imovel-update"),
    path("imovel/delete/<int:pk>/", ImovelDestroyAPIView.as_view(), name="imovel-delete"),
    
    # Estabelece os end-points para a Tabela IMOBILIARIA ----------------------------------------------#

    path("imobiliaria/", ImobiliariaListAPIView.as_view(), name="imobiliaria-list"),
    path("imobiliaria/create", ImobiliariaCreateAPIView.as_view(),name="imobiliaria-create"),
    path("imobiliaria/detail/<int:pk>/", ImobiliariaDetailAPIView.as_view(), name="imobiliaria-detail"),
    path("imobiliaria/update/<int:pk>/", ImobiliariaUpdateAPIView.as_view(), name="imobiliaria-update"),
    path("imobiliaria/delete/<int:pk>/", ImobiliariaDestroyAPIView.as_view(), name="imobiliaria-delete"),
    # --------------------------------------------------------------------------------------------------#
]
