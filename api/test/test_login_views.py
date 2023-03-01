"""_summary_
    EasyBio API Views test
"""
import logging
from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import *
from api.serializer import *
from api.test.utils import CustomIniDataToken
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

@tag('login')
class TokeViewTestCase(APITestCase):
    def setUp(self):
        logger.debug("SETUP {}".format(str(self.__class__.__name__)))
        return super().setUp()
        
    def test_token_general_post(self):
        _token_data = CustomIniDataToken.init_general_mobile_token(None)
        url = reverse("api:token-general")
        r = self.client.post(url, _token_data, format="json")
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)

    def test_token_general_post_error(self):
        _token_data = CustomIniDataToken.init_general_mobile_token(datetime.utcnow()+timedelta(seconds=-31))
        url = reverse("api:token-general")
        r = self.client.post(url, _token_data, format="json")
        logger.debug("TOKEN R DATA: {}".format(str(r.status_code)))
        self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)

#Llenar datos de prueba
#e= EstadoViewTestCase()
#e.setUp()

    # puppies = Puppy.objects.all()
    # serializer = PuppySerializer(puppies, many=True)
    # self.assertEqual(response.data, serializer.data)
    # self.assertEqual(response.status_code, status.HTTP_200_OK)        
               
