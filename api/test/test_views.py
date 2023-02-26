"""_summary_
    EasyBio API Views test
"""
import logging
from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework import status
from django.utils.http import urlencode
from django.urls import reverse
from api.models import *
from api.serializer import *
from django.db.models.query_utils import Q
from api.test.utils import CustomIniDataClass
from inspect import currentframe

logger = logging.getLogger(__name__)

class GenericViewTestCase(APITestCase, CustomIniDataClass):
    # def __init__(self, object_class, serializer_class, 
    #             instance_class, reverse_name_detail,
    #             reverse_name_list, serialized_data_object):
    #     self.object_class = object_class
    #     self.serializer_class = serializer_class
    #     self.reverse_name_detail = reverse_name_detail
    #     self.reverse_name_list = reverse_name_list
    #     self.instance_class = instance_class
    #     self.serialized_data_object = serialized_data_object
    #     super().__init__()

    def setUp(self, object_class, serializer_class, 
                reverse_name_detail, reverse_name_list,
                serialized_data_object, reverse_extra_param,
                filter_condition,
                parent_instance_class)-> None:
        self.init_data_test()
        self.object_class = object_class
        self.serializer_class = serializer_class
        self.reverse_name_detail = reverse_name_detail
        self.reverse_name_list = reverse_name_list
        self.instance_class = self.object_class.objects.all().first()
        self.serialized_data_object = serialized_data_object        
        self.reverse_extra_param = reverse_extra_param,
        self.filter_condition = filter_condition
        self.parent_instance_class = parent_instance_class
        return super().setUp()    

    def generic_test_detalle_get(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_detail, kwargs={'id':self.instance_class.id})
        r = self.client.get(url)
        current_objects= self.object_class.objects.get(pk=self.instance_class.id)
        serializer = self.serializer_class(current_objects)
        self.assertEqual(r.data,serializer.data)
        self.assertEqual(r.status_code,status.HTTP_200_OK)
 
    def generic_test_detalle_get_error(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_detail, kwargs={'id':1000})
        r = self.client.get(url)
        self.assertEqual(r.status_code,status.HTTP_404_NOT_FOUND)

    def generic_test_detalle_put(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_detail, kwargs={'id':self.instance_class.id})
        serializer = self.serializer_class(self.instance_class, many = False)
        r = self.client.put(url, serializer.data, format="json")
        self.assertEqual(r.status_code,status.HTTP_200_OK)

    def generic_test_detalle_put_error(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_detail, kwargs={'id':1000})
        serializer = self.serializer_class(self.instance_class, many = False)
        r = self.client.put(url, serializer.data, format="json")
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
            
    def generic_test_detalle_delete(self):
        logger.debug(str(self.object_class))
        self.instance_class = self.object_class.objects.create(**self.serialized_data_object)
        url = reverse(self.reverse_name_detail, kwargs={'id':self.instance_class.id})
        r = self.client.delete(url)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)

    def generic_test_detalle_delete_error(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_detail, kwargs={'id':1000})
        r = self.client.delete(url)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

    def generic_test_listados_get(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_list)
        if self.reverse_extra_param and self.filter_condition and self.parent_instance_class:
            _parent_instance = self.parent_instance_class.objects.all().first()
            url = "{}?parent_id={}".format(url,_parent_instance.id)
            self.filter_condition.update({list(self.filter_condition.keys())[0]: _parent_instance.id})
            current_objects= self.object_class.objects.filter(Q(**self.filter_condition))
        else:
            current_objects= self.object_class.objects.all()            
        r = self.client.get(url)
        serializer = self.serializer_class(current_objects,  many =True)
        self.assertEqual(r.data,serializer.data)
        self.assertEqual(r.status_code,status.HTTP_200_OK)
            
    def generic_test_post(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_list)
        self.instance_class = self.object_class(**self.serialized_data_object)
        serializer = self.serializer_class(self.instance_class, many = False)
        r = self.client.post(url, serializer.data, format="json")
        self.instance_class = self.object_class.objects.get(pk=r.data["id"])
        serializer = self.serializer_class(self.instance_class, many = False)
        self.assertEqual(r.data,serializer.data)
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)

    def generic_test_post_error(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_list)
        r = self.client.post(url, None)
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)

class EstadoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Estado, serializer_class = EstadoSerializer,
                    reverse_name_detail = "api:estado-detalle", 
                    reverse_name_list = "api:estado",
                    serialized_data_object = {"descripcion": "Final", "color": '00FF00',},
                    reverse_extra_param=False, 
                    filter_condition=None,
                    parent_instance_class=None
                    )
        
    def test_detalle_get(self): self.generic_test_detalle_get()

    def test_detalle_get_error(self): self.generic_test_detalle_get_error()

    def test_detalle_put(self): self.generic_test_detalle_put()

    def test_detalle_put_error(self): self.generic_test_detalle_put_error()

    def test_detalle_delete(self): self.generic_test_detalle_delete()

    def test_detalle_delete_error(self): self.generic_test_detalle_delete_error()

    def test_listados_get(self): self.generic_test_listados_get()

    def test_post(self): self.generic_test_post()

    def test_post_error(self): self.generic_test_post_error()

class DepartamentoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Departamento, serializer_class = DepartamentoSerializer,
                    reverse_name_detail = "api:departamento-detalle", 
                    reverse_name_list = "api:departamento",
                    serialized_data_object = {
                        "empresa_id":1,
                        "descripcion": "Talento Humano",
                        "estado_id": 1,
                        },
                    reverse_extra_param=True, 
                    filter_condition={"empresa__id":0},
                    parent_instance_class=Empresa
                    )
        
    def test_detalle_get(self): self.generic_test_detalle_get()

    def test_detalle_get_error(self): self.generic_test_detalle_get_error()

    def test_detalle_put(self): self.generic_test_detalle_put()

    def test_detalle_put_error(self): self.generic_test_detalle_put_error()

    def test_detalle_delete(self): self.generic_test_detalle_delete()

    def test_detalle_delete_error(self): self.generic_test_detalle_delete_error()

    def test_listados_get(self): self.generic_test_listados_get()

    def test_post(self): self.generic_test_post()

    def test_post_error(self): self.generic_test_post_error()

class EmpresaViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Empresa, serializer_class = EmpresaSerializer,
                    reverse_name_detail = "api:empresa-detalle", 
                    reverse_name_list = "api:empresa",
                    serialized_data_object = {
                        "ruc": "2222222222222",
                        "razon_social": "Empresa Dos",
                        "nombre_comercial": "Empresa Dos comercial",
                        "direccion": "direccion dos",
                        "telefono": "telefono dos",
                        "nombres_contacto": "nombres contacto dos",
                        "cargo_contacto": "cargo contacto dos",
                        "email_contacto": "prueba@dos.com",
                        "telefono_contacto": "2222222",
                        "inicio_contrato": "2023-01-01",
                        "fin_contrato": "2023-12-31",
                        "estado_id": 1,
                        },
                    reverse_extra_param=False, 
                    filter_condition=None,
                    parent_instance_class=None
                    )
        
    def test_detalle_get(self): self.generic_test_detalle_get()

    def test_detalle_get_error(self): self.generic_test_detalle_get_error()

    def test_detalle_put(self): self.generic_test_detalle_put()

    def test_detalle_put_error(self): self.generic_test_detalle_put_error()

    def test_detalle_delete(self): self.generic_test_detalle_delete()

    def test_detalle_delete_error(self): self.generic_test_detalle_delete_error()

    def test_listados_get(self): self.generic_test_listados_get()

    def test_post(self): self.generic_test_post()

    def test_post_error(self): self.generic_test_post_error()

#Llenar datos de prueba
# e= EstadoViewTestCase()
# e.setUp()

    # puppies = Puppy.objects.all()
    # serializer = PuppySerializer(puppies, many=True)
    # self.assertEqual(response.data, serializer.data)
    # self.assertEqual(response.status_code, status.HTTP_200_OK)        
               
