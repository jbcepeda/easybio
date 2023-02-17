"""_summary_
    EasyBio API test
"""

"""_summary_
    API Model test
"""

from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Estado

# Create your tests here.
class EstadoTestCase(APITestCase):
    def setUp(self) -> None:
        self.estado = Estado.objects.create(descripcion = "Inicial", color = '0000FF')
        return super().setUp()
    
    def test_estado_list(self):
        url = reverse("api:estado")
        r = self.client.get(url)
        self.assertContains(r,"Inicial")
        

