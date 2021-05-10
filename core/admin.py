from django.contrib import admin
from core.models import Imovel, Imobiliaria

"""
    Neste arquivo é configurado o Painel Administrativo do programa.
    O Django usa um padrao ja pre estabelecido para padronizar
    este sistema de Admin.

    Ele precisa de todos os Models importados para que estas
    venham a ser usados dentro do seu sistema de Admin.

    Nele é possivel realizar, dentre muitas outras coisas, a 
    listagem​, cadastro​, edição​ e d​eleção​ das entidades repesentadas por 
    meio dos models importados.

    Tambem é possivel criar novos usuarios e novos grupos de permissao
    de uma maneira muito rapida e util.
    
    => https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

"""

admin.site.register(Imovel)
admin.site.register(Imobiliaria)
