from django.test import TestCase
from message.models import Comentario

class ComentarioTestCase(TestCase):
    def test_key(self):
        Comentario.objects.create(titulo_del_comentario = "hola")

