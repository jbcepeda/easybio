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
import json
from api.test.generic_view_test_class import CustomIniDataClass

logger = logging.getLogger(__name__)

@tag('auth')
class GeneralTokenViewTestCase(APITestCase):
    def setUp(self):
        logger.debug("SETUP {}".format(str(self.__class__.__name__)))
        return super().setUp()
        
    def test_general_token_post(self):
        _local_mobile_data = CustomIniDataToken.init_general_mobile_data(None)
        url = reverse("api:token-general")
        r = self.client.post(url, _local_mobile_data, format="json")
        logger.debug("test_general_token_post DATA {}".format(r.data))
        self.assertEqual(r.status_code,status.HTTP_200_OK)

    def test_general_token_post_error(self):
        _local_mobile_data = CustomIniDataToken.init_general_mobile_data(datetime.utcnow()+timedelta(seconds=-31))
        url = reverse("api:token-general")
        r = self.client.post(url, _local_mobile_data, format="json")
        logger.debug("TOKEN R DATA: {}".format(str(r)))
        self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)

@tag('auth')
class BioLoginViewTestCase(APITestCase, CustomIniDataClass):
    def setUp(self):
        logger.debug("SETUP {}".format(str(self.__class__.__name__)))
        self.init_data_test()
        return super().setUp()
        
    def test_bio_login_post(self):
        _local_mobile_data = CustomIniDataToken.init_general_mobile_data(None)
        url = reverse("api:token-general")
        r = self.client.post(url, _local_mobile_data, format="json")
        _server_token_data = CustomIniDataToken.get_token_info(r.data)
        url = reverse("api:bio-login")
        eid = '0600000000'
        _source_path = Path.joinpath(settings.BASE_DIR, "tmp","foto_otro_benja.jpeg")
        with open(_source_path, "rb") as img_file:
            f = base64.b64encode(img_file.read())
        _bio_data = {
                "eid": eid,
                "f": f.decode('utf-8')                
            }
        _data = {
            "token": _server_token_data, 
            "data":_bio_data,                
        }
        _data = json.dumps(_data)
        _data = CustomIniDataToken.encrypt(_data)
        r = self.client.post(url, _data, format="json")
        self.assertEqual(r.status_code,status.HTTP_200_OK)

    def test_bio_login_post_error(self):
        _local_mobile_data = CustomIniDataToken.init_general_mobile_data(None)
        url = reverse("api:token-general")
        r = self.client.post(url, _local_mobile_data, format="json")
        _server_token_data = CustomIniDataToken.get_token_info(r.data)
        url = reverse("api:bio-login")
        eid = '0600000000'
        _source_path = Path.joinpath(settings.BASE_DIR, "tmp","foto_alejo.jpeg")
        with open(_source_path, "rb") as img_file:
            f = base64.b64encode(img_file.read())
        _bio_data = {
                "eid": eid,
                "f": f.decode('utf-8')                
            }
        _data = {
            "token": _server_token_data, 
            "data":_bio_data,                
        }
        _data = json.dumps(_data)
        _data = CustomIniDataToken.encrypt(_data)
        r = self.client.post(url, _data, format="json")
        self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)

#Llenar datos de prueba
#e= EstadoViewTestCase()
#e.setUp()

