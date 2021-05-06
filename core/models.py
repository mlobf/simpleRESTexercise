from django.db import models


class Imoveis(models.Model):
    class Meta:
        ordering = ["id", "nome"]

    nome = models.CharField(max_length=255, null=False, blank=False)
      #Link para o endereço
    alias = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alias


class Endereco(models.Model):
    class Meta:
        ordering = ["id"]
    
    estado  = models.CharField(max_length=255, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    bairro = models.CharField(max_length=255, null=False, blank=False)
    rua = models.CharField(max_length=255, null=False, blank=False)
    numero = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.id


class Imobiliaria(models.Model):
      class Meta:
        ordering = ["id", "nome"]
        
      nome = models.CharField(max_length=255, null=False, blank=False)
      #Link para o endereço