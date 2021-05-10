from rest_framework import serializers
from core.models import Imovel, Imobiliaria


class ImobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imobiliaria
        fields = ["id", "nome", "endereço"]


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = [
            "id",
            "nome",
            "endereco",
            "descricao",
            "status",
            "caracteristicas",
            "tipo",
            "finalidade",
            "imobiliaria",
        ]
