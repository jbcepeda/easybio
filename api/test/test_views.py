"""_summary_
    EasyBio API Views test
"""
import logging
from api.models import *
from api.serializer import *
from api.test.utils import CustomIniDataClass
from api.test.generic_view_test_class import GenericViewTestCase
from django.contrib.auth.hashers import make_password

logger = logging.getLogger(__name__)

class EstadoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Estado, serializer_class = EstadoSerializer,
                    reverse_name_detail = "api:estado-detalle", 
                    reverse_name_list = "api:estado",
                    serialized_data_object = {"descripcion": "Nuevo Estado", "color": '00FF00',},
                    update_data_fields= {'descripcion': 'Desactivado',},
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
                        "descripcion": "Nuevo Departamento",
                        "estado_id": 1,
                        },
                    update_data_fields= {'descripcion': 'Talento Humano',},                    
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
                        "razon_social": "Nuevo Nombre Empresa",
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
                    update_data_fields= {'razon_social': 'Empresa DOS',},                                        
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

class TipoEventoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = TipoEvento, serializer_class = TipoEventoSerializer,
                    reverse_name_detail = "api:tipo-evento-detalle", 
                    reverse_name_list = "api:tipo-evento",
                    serialized_data_object = {
                        "empresa_id": 1,
                        "descripcion": "Nuevo Tipo Evento",
                        "orden": 1,
                        "estado_id": 1,
                        },
                    update_data_fields= {'descripcion': 'FIN Jornada laboral',},                    
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

class UbicacionViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Ubicacion, serializer_class = UbicacionSerializer,
                    reverse_name_detail = "api:ubicacion-detalle", 
                    reverse_name_list = "api:ubicacion",
                    serialized_data_object = {
                        "empresa_id": 1,
                        "descripcion": "Nuevo Ubicacion",
                        "tipo_dato":  "point",
                        "coordenadas": [{"lat":-0.19041117621469852, "lon":-78.48837800323963}],
                        "distancia_max":  20,
                        "estado_id": 1,
                        },
                    update_data_fields= {'descripcion': 'RPDMQ',},                    
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

class EmpleadoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Empleado, serializer_class = EmpleadoSerializer,
                    reverse_name_detail = "api:empleado-detalle", 
                    reverse_name_list = "api:empleado",
                    serialized_data_object = {
                        "cedula": '0600000000',
                        "nombres":  'Benjamin',
                        "apellidos": 'Nuevo Apellidos',
                        "foto": None,
                        "celular": '0999999999',
                        "departamento_id": 1,
                        "ubicacion_id": 1,
                        "estado_id": 1,
                        },
                    update_data_fields= {'apellidos': 'Cepeda',},                    
                    reverse_extra_param=True, 
                    filter_condition={"departamento__empresa__id":0},
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

class PerfilViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Perfil, serializer_class = PerfilSerializer,
                    reverse_name_detail = "api:perfil-detalle", 
                    reverse_name_list = "api:perfil",
                    serialized_data_object = {
                        'descripcion': 'Nuevo Perfil',
                        'es_administrador': 1,
                        'estado_id':1,                        
                        },
                    update_data_fields= {'descripcion': 'Supervisor',},
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

class UsuarioViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Usuario, serializer_class = UsuarioSerializer,
                    reverse_name_detail = "api:usuario-detalle", 
                    reverse_name_list = "api:usuario",
                    serialized_data_object = {
                        'nombre_usuario': 'nuevousuario',
                        'empleado_id': 1,
                        'clave': '1234',
                        'perfil_id': 1,
                        'estado_id': 1,
                    },
                    update_data_fields= {'nombre_usuario': 'aiza',
                                         "clave": "123456"},                    
                    reverse_extra_param=True, 
                    filter_condition={"empleado__ubicacion__empresa__id":0},
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


#Llenar datos de prueba
#e= EstadoViewTestCase()
#e.setUp()

    # puppies = Puppy.objects.all()
    # serializer = PuppySerializer(puppies, many=True)
    # self.assertEqual(response.data, serializer.data)
    # self.assertEqual(response.status_code, status.HTTP_200_OK)        
               
