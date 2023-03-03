"""_summary_
    EasyBio API Views test
"""
import logging
from django.test import tag
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase
from api.aws_services_connect import AWSServicesConnect
import base64
from pathlib import Path

logger = logging.getLogger(__name__)

@tag('aws')
class TokeViewTestCase(APITestCase):
    def setUp(self):
        logger.debug("SETUP {}".format(str(self.__class__.__name__)))
        return super().setUp()
    
    def test_aws_rekognition_service(self):
        _source_path = Path.joinpath(settings.BASE_DIR, "tmp","foto_otro_benja.jpeg")
        _target_path = Path.joinpath(settings.BASE_DIR, "tmp","foto_serio.jpeg") 
        with open(_source_path, "rb") as img_file:
            source_data = base64.b64encode(img_file.read())

        with open(_target_path, "rb") as img_file:
            target_data = base64.b64encode(img_file.read())        
        _is_match, _match_details =  AWSServicesConnect.compare_faces(self,
            source_base64=source_data, 
            target_base64=target_data)
        logger.debug("test_aws_rekognition_service  {} {}".format(_is_match, _match_details))
        self.assertEqual(_is_match,True)
