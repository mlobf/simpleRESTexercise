from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Endereco(models.Model):
    class Meta:
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"

    estado = models.CharField(max_length=255, null=False, blank=False)  # Obrigatorio
    cidade = models.CharField(max_length=255, null=False, blank=False)  # Obrigatorio
    bairro = models.CharField(max_length=255, null=False, blank=False)  # Obrigatorio
    rua = models.CharField(max_length=255, null=False, blank=False)  # Obrigatorio
    complemento = models.CharField(max_length=255, null=False, blank=False)
    cep = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(
            self.estado,
            self.cidade,
            self.bairro,
            self.rua,
            self.complemento,
            self.cep,
        )


class Imobiliaria(models.Model):
    class Meta:
        ordering = ["id", "nome"]
        verbose_name = "Imobiliaria"
        verbose_name_plural = "Imobiliarias"

    nome = models.CharField(max_length=255, null=False, blank=False)  # Obrigatorio
    endereco = models.ManyToManyField(Endereco, related_name="imobiliaria_endereco")
    # contato = models.CharField(max_length=255, null=False, blank=False)
    # telefone = models.CharField(max_length=255, null=False, blank=False)
    # status = models.BooleanField(default=True)  #
    # imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name="imobiliaria")
    # imovel = models.ManyToManyField(Imovel, related_name="Imoveis")

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    class Meta:
        ordering = ["id", "nome"]
        verbose_name = "Imovel"
        verbose_name_plural = "Imoveis"

    nome = models.CharField(max_length=255, null=False, blank=False)  # Obrigatorio
    # descricao = models.TextField(max_length=255, null=False, blank=False)  # Obrigatorio
    # status = models.BooleanField(default=True, blank=False)  # Obrigatorio
    # caracteristicas = models.CharField(max_length=255, null=False, blank=False)
    # tipo = models.CharField(max_length=255, null=False, blank=False)
    # finalidade = models.CharField(max_length=255, null=False, blank=True)  # finalidade
    # Link to Imobiliaria
    imobiliaria = models.ManyToManyField(Imobiliaria, related_name="Imobiliarias")
    endereco = models.ManyToManyField(Endereco, related_name="imovel_endereco")

    def __str__(self):
        return self.nome
