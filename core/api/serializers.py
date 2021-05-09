from rest_framework import serializers
from core.models import Imovel, Imobiliaria


class ImobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imobiliaria
        fields = ["name", "endereço"]


class ImovelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imovel
        fields = [
            "id",
            "nome",
            "status",
            "tipo",
            "finalidade",
            "endereco",
            "imobiliaria",
        ]
