from rest_framework import serializers
from core.models import Imobiliaria, Imovel


"""
    Processo de "transformação" de determinados campos da Tabela em JSON.

    Atraves da Classe Meta é possivel determinal:
        ->model = O nome da Tabela.
        ->fields = Os campos a serem transformados em JSON da respectiva Tabela.

"""


# Esta Classe realiza o processo de serializacao da tabela Imobiliaria.
class ImobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imobiliaria
        # Seleciona os campos a ser serializados da tabela Imobiliaria.
        fields = ["id", "nome", "endereço"]


# Esta Classe realiza o processo de serializacao da tabela Imovel.
class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        # Seleciona os campos a ser serializados da tabela Imovel.
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
