from rest_framework.test import APITestCase
from api.test.utils import CustomIniDataClass
import logging
from rest_framework import status
from django.urls import reverse
from django.db.models.query_utils import Q

logger = logging.getLogger(__name__)

class GenericViewTestCase(APITestCase, CustomIniDataClass):

    def setUp(self, object_class, serializer_class, 
                reverse_name_detail, reverse_name_list,
                serialized_data_object, update_data_fields, 
                reverse_extra_param, filter_condition,
                parent_instance_class)-> None:
        self.init_data_test()
        self.object_class = object_class
        self.serializer_class = serializer_class
        self.reverse_name_detail = reverse_name_detail
        self.reverse_name_list = reverse_name_list
        self.instance_class = self.object_class.objects.all().last()
        self.serialized_data_object = serialized_data_object        
        self.update_data_fields = update_data_fields
        self.reverse_extra_param = reverse_extra_param,
        self.filter_condition = filter_condition
        self.parent_instance_class = parent_instance_class
        codigo = self.instance_class.id
        if self.reverse_extra_param and parent_instance_class:
            codigo = self.parent_instance_class.objects.all().last().id
        for k, v in self.serialized_data_object.items():
            if "_id" in k:
                self.serialized_data_object[k] = codigo
        logger.debug("NUEVOS VALORES: {}".format(self.serialized_data_object))
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
        put_data = serializer.data
        for k, v in self.update_data_fields.items():
            put_data[k] = v
        r = self.client.put(url, put_data, format="json")
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
        self.instance_class = self.object_class.objects.all().last()
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
        logger.debug("Empresa: {} Departamento: {} Calendario:{} Estado: {} ubicacion: {}".
                     format(self.empresa.id, self.departamento.id, self.calendario.id, self.estado.id, self.ubicacion))
        serializer = self.serializer_class(self.instance_class, many = False)
        logger.debug("POST-BEFORE: {}".format(str(serializer.data)))
        r = self.client.post(url, serializer.data, format="json")
        # logger.debug("POST-Resultado: {}".format(str(r.data)))
        self.instance_class = self.object_class.objects.get(pk=r.data["id"])
        serializer = self.serializer_class(self.instance_class, many = False)
        self.assertEqual(r.data,serializer.data)
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)

    def generic_test_post_error(self):
        logger.debug(str(self.object_class))
        url = reverse(self.reverse_name_list)
        r = self.client.post(url, None)
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
