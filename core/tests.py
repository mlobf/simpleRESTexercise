from django.test import TestCase
from .models import Imovel, Imobiliaria


class ImobiliariaTestCase(TestCase):
    def setUp(self):
        Imobiliaria.objects.create(nome="Nova", endereço="Rua 25 de nov")

    def test_imobiliaria(self):
        nova = Imobiliaria.objects.get(nome="Nova")





    """
    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
    """
