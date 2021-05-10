from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

"""
    Neste arquivo é elaborado o ORM -Object-relational mapping.

    Assim como no Flask nos temos o SQLAlchemy, no Django nos
    temos o seu proprio ORM pronto para uso, seguindo a linha 
    'Batteries included'.
    
    => https://docs.djangoproject.com/en/2.2/topics/db/models/

    Cada classe representa uma Tabela no qual, por meio da 
    classe Meta, é possivel estabelecer alguns comportamentos
    já configurados.
    
    Exemplo:
        ordering = ["nome"]

    Seus campos da Tabela podem ser estabelecidos adicionando variaveis
    e atribuindo a estas, as respectivas finalidades.
    
    Exemplo:

    nome = sera um campo texto com as seguintes caracteristicas.
    preço = sera um campo currency com as seguintes caracteristicas.
"""


# Finalidade----------------------#
RESIDENCIAL = "residencial"
COMERCIAL = "comercial"

FINALIDADE = (
    (RESIDENCIAL, "Residencial"),
    (COMERCIAL, "Comercial"),
)
# Status---------------------------#
ATIVO = "ativo"
INATIVO = "inativo"

STATUS = (
    (ATIVO, "Ativo"),
    (INATIVO, "Inativo"),
)
# Tipo de Residencia----------------#
CASA = "casa"
APARTAMENTO = "apartamento"

TIPO = (
    (CASA, "Casa"),
    (APARTAMENTO, "Apartamento"),
)


class Imobiliaria(models.Model):
    class Meta:
        ordering = ["nome"]
        verbose_name = "Imobiliaria"
        verbose_name_plural = "Imobiliarias"

    # Determina os campos nome e endereço na tabela Imobiliaria.
    nome = models.CharField(max_length=255, null=False, blank=False)  # Obrigatorio
    endereço = models.CharField(max_length=255, null=True, blank=True)  # Obrigatorio

    # Retorna o seguinte campo nome quando o objeto for chamado.
    def __str__(self):
        return self.nome


class Imovel(models.Model):
    class Meta:
        ordering = ["nome"]
        verbose_name = "Imovel"
        verbose_name_plural = "Imoveis"

    nome = models.CharField(max_length=100, null=False, blank=False)  # Obrigatorio
    endereco = models.CharField(max_length=100, null=False, blank=False)  # Obrigatorio
    descricao = models.TextField(max_length=255, null=False, blank=False)  # Obrigatorio
    status = models.CharField(choices=STATUS, max_length=20)  #
    caracteristicas = models.TextField(max_length=255, null=True, blank=True)
    tipo = models.CharField(choices=TIPO, max_length=20)  #
    finalidade = models.CharField(choices=FINALIDADE, max_length=20)
    imobiliaria = models.ForeignKey(
        Imobiliaria,
        on_delete=models.SET("1"),
        null=False,
        related_name="imobiliaria",
    )

    # Retorna o seguinte campo nome quando o objeto for chamado.
    def __str__(self):
        return self.nome
