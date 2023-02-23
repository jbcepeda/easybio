"""_summary_
    EasyBio API Views test
"""
import logging
from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from api.models import *
from api.serializer import *

logger = logging.getLogger(__name__)

def init_data_test(self) -> None:
    self.estado = Estado.objects.create(descripcion = "Inicial", color = '0000FF')
    self.empresa = Empresa.objects.create(
        ruc = "1111111111111",
        razon_social = "Empresa Uno",
        nombre_comercial = "Empresa uno comercial",
        direccion = "direccion uno",
        telefono = "telefono uno",
        nombres_contacto = "nombres contacto uno",
        cargo_contacto = "cargo contacto uno",
        email_contacto = "prueba@uno.com",
        telefono_contacto = "2222221",
        inicio_contrato = "2023-01-01",
        fin_contrato = "2023-12-31",
        estado = self.estado
        )

    self.tipo_evento = TipoEvento.objects.create(
        empresa = self.empresa,
        descripcion = "Inicio Jornada laboral",
        orden = 1,
        estado = self.estado
    )

    self.departamento = Departamento.objects.create(
        empresa = self.empresa,
        descripcion = "Sistemas",
        estado = self.estado
    )

    self.ubicacion = Ubicacion.objects.create(
        empresa = self.empresa,
        descripcion = "RPDMQ",
        tipo_dato =  "point",
        coordenadas = [{"lat":-0.19041117621469852, "lon":-78.48837800323963}],
        distancia_max =  20,
        estado = self.estado
    )
    
    self.empleado = Empleado.objects.create(
        cedula = '0600000000',
        nombres = 'Benjamin',
        apellidos = 'Cepeda',
        foto = None,
        celular = '0999999999',
        departamento = self.departamento,
        ubicacion = self.ubicacion,
        estado = self.estado
    )
    
    self.perfil = Perfil.objects.create(
        descripcion = 'Empleado',
        es_administrador = 0,
        estado = self.estado
    )
    
    self.usuario =  Usuario.objects.create(
        nombre_usuario = 'bcepeda',
        empleado = self.empleado,
        clave = '1234',
        perfil = self.perfil,
        estado = self.estado
    )
    

class EstadoViewTestCase(APITestCase):
    def setUp(self) -> None:
        init_data_test(self=self)
        return super().setUp()    

    def test_estado_detalle_get(self):
        url = reverse("api:estado-detalle",kwargs={'id':self.estado.id})
        r = self.client.get(url)
        self.assertContains(r,"Inicial")
 
    def test_estado_detalle_get_error(self):
        url = reverse("api:estado-detalle",kwargs={'id':1000})
        r = self.client.get(url)
        logger.debug(r.status_code)
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)

    def test_estado_detalle_put(self):
        url = reverse("api:estado-detalle",kwargs={'id':self.estado.id})
        serializer = EstadoSerializer(self.estado, many = False)
        r = self.client.put(url, serializer.data)
        self.assertEqual(r.status_code,status.HTTP_200_OK)

    def test_estado_detalle_put_error(self):
        url = reverse("api:estado-detalle",kwargs={'id':1000})
        serializer = EstadoSerializer(self.estado, many = False)
        r = self.client.put(url, serializer.data)
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)
            
    def test_estado_detalle_delete(self):
        self.estado = Estado.objects.create(descripcion = "Desactivado", color = '0000FF')
        url = reverse("api:estado-detalle",kwargs={'id':self.estado.id})
        r = self.client.delete(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_estado_detalle_delete_error(self):
        url = reverse("api:estado-detalle",kwargs={'id':1000})
        r = self.client.delete(url)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

    def test_estados_get(self):
        url = reverse("api:estado")
        r = self.client.get(url)
        self.assertContains(r,"Inicial")
            
    def test_estados_post(self):
        url = reverse("api:estado")
        self.estado.descripcion = 'Adicional'
        serializer = EstadoSerializer(self.estado, many = False)
        r = self.client.post(url, serializer.data)
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)

    def test_estados_post_error(self):
        url = reverse("api:estado")
        r = self.client.post(url, None)
        self.assertEqual(r.status_code,status.HTTP_400_BAD_REQUEST)

    # puppies = Puppy.objects.all()
    # serializer = PuppySerializer(puppies, many=True)
    # self.assertEqual(response.data, serializer.data)
    # self.assertEqual(response.status_code, status.HTTP_200_OK)        
               
class EmpresaTestCase(APITestCase):
    def setUp(self) -> None:
        init_data_test(self=self)
        return super().setUp()
    
    def test_empresa_list(self):
        url = reverse("api:empresa")
        r = self.client.get(url)
        self.assertContains(r,"Empresa Uno")
        
    def test_empresa_detalle(self):
        url = reverse("api:empresa-detalle",kwargs={'id':self.empresa.id})
        r = self.client.get(url)
        self.assertContains(r,"Empresa Uno")                
