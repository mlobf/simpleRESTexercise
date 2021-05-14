from django.test import TestCase
from .models import Imovel, Imobiliaria


class ImobiliariaTestCase(TestCase):
    def setUp(self):
        Imobiliaria.objects.create(nome="Imovel Web", endereço="Rua 25 de nov")
        imobilaria = Imobiliaria.objects.filter(nome="Imovel Web")

    def test_imobiliaria(self):
        new_test_create_imobiliaria = Imobiliaria.objects.get(nome="Imovel Web")

'''
class ImovelTestCase(TestCase):

    def test_imobiliaria(self):
        new_test_create_imobiliaria = Imobiliaria.objects.get(nome="Imovel Web")


    def setUp(self):
        Imovel.objects.create(
            nome="Imovel Web",
            endereco="Rua 25 de nov",
            descricao="Uma cada muito bonita",
            status="Residencial",
            caracteristicas="Dois quartos e 3 banheiros",
            tipo="ativo",
            finalidade="Comercial",
            imobiliaria=models.SET('1')

class UrlsTestCase(TestCase):
    """Testing all urls of the system"""

    def test_url_imovel_list(self):
        """
        Testing if the imovel list  is working
        """
        response = self.client.get("/api/imovel/")
        self.assertEqual(response.status_code, 200)

    def test_url_imovel_detail(self):
        """
        Testing if the imovel detail is working
        """
        response = self.client.get("/api/imovel/detail/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_imobiliaria_list(self):
        """
        Testing if the imobilaria list is working
        """
        response = self.client.get("/api/imobiliaria/")
        self.assertEqual(response.status_code, 200)

    def test_url_imobiliaria_detail(self):
        """
        Testing if the imobilaria detail is working
        """
        response = self.client.get("/api/imobiliaria/detail/1/")
        self.assertEqual(response.status_code, 200)
'''
