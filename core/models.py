from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Imovel(models.Model):
    class Meta:
        ordering = ["id", "nome"]
        verbose_name = "Imovel"
        verbose_name_plural = "Imoveis"

    nome = models.CharField(max_length=255, null=False, blank=False)  #
    # descricao = models.TextField(max_length=255, null=False, blank=False)  #
    # status = models.BooleanField(default=True)  #
    # caracteristicas = models.CharField(max_length=255, null=False, blank=False)
    # finalidade = models.CharField(max_length=255, null=False, blank=False)
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
    # contato = models.CharField(max_length=255, null=False, blank=False)
    # telefone = models.CharField(max_length=255, null=False, blank=False)
    # status = models.BooleanField(default=True)  #

    # imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name="imobiliaria")
    imovel = models.ForeignKey(Imovel, models.SET_NULL, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
