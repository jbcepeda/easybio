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
from api.auth_features.util import ApiCrypto
from datetime import datetime, timedelta
from pathlib import Path
from django.conf import settings
import base64

logger = logging.getLogger(__name__)

@tag('auth1')
class GeneralTokenViewTestCase(APITestCase):
    def setUp(self):
        logger.debug("SETUP {}".format(str(self.__class__.__name__)))
        return super().setUp()
        
    def test_general_token_post(self):
        _token_data = CustomIniDataToken.init_general_mobile_token(None)
        url = reverse("api:token-general")
        r = self.client.post(url, _token_data, format="json")
        logger.debug("test_general_token_post DATA {}".format(r.data))
        self.assertEqual(r.status_code,status.HTTP_200_OK)

    def test_general_token_post_error(self):
        _token_data = CustomIniDataToken.init_general_mobile_token(datetime.utcnow()+timedelta(seconds=-31))
        url = reverse("api:token-general")
        r = self.client.post(url, _token_data, format="json")
        logger.debug("TOKEN R DATA: {}".format(str(r.status_code)))
        self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)

@tag('auth2')
class CompanyTokenViewTestCase(APITestCase):
    def setUp(self):
        logger.debug("SETUP {}".format(str(self.__class__.__name__)))
        return super().setUp()
        
    def test_login_app_post(self):
        _token_data = CustomIniDataToken.init_general_mobile_token(None)
        url = reverse("api:token-general")
        r = self.client.post(url, _token_data, format="json")
        
        url = reverse("api:bio-login")
        d = r.data["d"]
        eid = '0602326787'
        _source_path = Path.joinpath(settings.BASE_DIR, "tmp","foto_otro_benja.jpeg")
        with open(_source_path, "rb") as img_file:
            f = base64.b64encode(img_file.read())
        _bio_data = {
                "eid": eid,
                "f": f                
            }
        data = ApiCrypto.crypt(data)
        m = {
            "data":_bio_data,                
            "token": t
        }
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)

    def test_general_token_post_error(self):
        _token_data = CustomIniDataToken.init_general_mobile_token(datetime.utcnow()+timedelta(seconds=-31))
        url = reverse("api:token-general")
        r = self.client.post(url, _token_data, format="json")
        logger.debug("TOKEN R DATA: {}".format(str(r.status_code)))
        self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)

#Llenar datos de prueba
#e= EstadoViewTestCase()
#e.setUp()

