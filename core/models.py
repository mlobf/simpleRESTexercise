from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Imovel(models.Model):
    class Meta:
        ordering = ["id", "nome"]
        verbose_name = "Imovel"
        verbose_name_plural = "Imoveis"

    nome = models.CharField(max_length=255, null=False, blank=False)  #
    descricao = models.TextField(max_length=255, null=False, blank=False)  #
    status = models.BooleanField(default=True)  #
    caracteristicas = models.CharField(max_length=255, null=False, blank=False)
    finalidade = models.CharField(max_length=255, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # Link to Imobiliaria

    def __str__(self):
        return self.nome


class Imobiliaria(models.Model):
    class Meta:
        ordering = ["id", "nome"]
        verbose_name = "Imobiliaria"
        verbose_name_plural = "Imobiliarias"

    nome = models.CharField(max_length=255, null=False, blank=False)
    contato = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=255, null=False, blank=False)
    status = models.BooleanField(default=True)  #
    imovel = models.ForeignKey(
        Imovel, on_delete=models.CASCADE, related_name="imobiliaria"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"

    estado = models.CharField(max_length=255, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    bairro = models.CharField(max_length=255, null=False, blank=False)
    rua = models.CharField(max_length=255, null=False, blank=False)
    numero = models.CharField(max_length=255, null=False, blank=False)
    cep = models.CharField(max_length=255, null=False, blank=False)

    # Date Field
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Tipo(models.Model):
    class Meta:
        ordering = ["id", "categoria"]
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

    categoria = models.CharField(max_length=255, null=False, blank=False)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name="tipo")
    status = models.BooleanField(default=True)  #
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoria
