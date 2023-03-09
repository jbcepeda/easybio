"""_summary_
    EasyBio API Views test
"""
import logging
from django.test import tag
from django.urls import reverse
from api.models import *
from api.serializer import *
from api.test.generic_view_test_class import GenericViewTestCase
import logging
from api.test.utils import CustomIniDataClass

logger = logging.getLogger(__name__)

@tag('views')
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

@tag('views')
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
                        "meses_disponible_datos": 3,
                        "permitir_uso_varios_dispositivos": "False",                        
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

@tag('views')
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

@tag('views')
class FeriadoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Feriado, serializer_class = FeriadoSerializer,
                    reverse_name_detail = "api:feriado-detalle", 
                    reverse_name_list = "api:feriado",
                    serialized_data_object = {
                        "empresa_id": 1,
                        "fecha": "2023-11-02",
                        "descripcion": "Dia difuntos",
                        "es_global": "True",
                        "estado_id": 1,
                        },
                    update_data_fields= {'descripcion': 'Día de los difuntos',},                    
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


@tag('views')
class CalendarioViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Calendario, serializer_class = CalendarioSerializer,
                    reverse_name_detail = "api:calendario-detalle", 
                    reverse_name_list = "api:calendario",
                    serialized_data_object = {
                        "empresa_id": 1,
                        "nombre": "Jornada Nocturna",
                        "descripcion": "Jornada semanal L-V 4pM-12PM",
                        "estado_id": 1,
                        },
                    update_data_fields= {'descripcion': 'Día de los difuntos',},                    
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

@tag('views')
class DiaViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Dia, serializer_class = DiaSerializer,
                    reverse_name_detail = "api:dia-detalle", 
                    reverse_name_list = "api:dia",
                    serialized_data_object = {
                        "calendario_id": 1,
                        "dia_semana": 7,
                        "estado_id": 1,
                        },
                    update_data_fields= {'dia_semana': 6,},                    
                    reverse_extra_param=True, 
                    filter_condition={"calendario__id":0},
                    parent_instance_class=Calendario
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

@tag('views')
class FranjaTiempoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = FranjaTiempo, serializer_class = FranjaTiempoSerializer,
                    reverse_name_detail = "api:franja-tiempo-detalle", 
                    reverse_name_list = "api:franja-tiempo",
                    serialized_data_object = {
                        "calendario_id": 1,
                        "descripcion": 'Horario nocturno trabajo 6PM a 12PM',
                        "es_laborable": "True",
                        "tiene_horario_fijo": "True",
                        "duracion_minutos": 0,
                        "hora_inicio": '18:00',
                        "hora_fin": '23:59',
                        "estado_id": 1,
                        },
                    update_data_fields= {'dia': 7,},                    
                    reverse_extra_param=True, 
                    filter_condition={"calendario__id":0},
                    parent_instance_class=Calendario
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

@tag('views')
class DiaFranjaTiempoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = DiaFranjaTiempo, serializer_class = DiaFranjaTiempoSerializer,
                    reverse_name_detail = "api:dia-franja-tiempo-detalle", 
                    reverse_name_list = "api:dia-franja-tiempo",
                    serialized_data_object = {
                    "dia_id": 3,
                    "franja_tiempo_id": 1,
                    "estado_id": 1
                        },
                    update_data_fields= {'dia_id': 4,},                    
                    reverse_extra_param=True, 
                    filter_condition={"franja_tiempo__id":0},
                    parent_instance_class=FranjaTiempo
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

@tag('views')
class UbicacionViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Ubicacion, serializer_class = UbicacionSerializer,
                    reverse_name_detail = "api:ubicacion-detalle", 
                    reverse_name_list = "api:ubicacion",
                    serialized_data_object = {
                        "empresa_id": 1,
                        "descripcion": "Nueva Ubicacion",
                        "tipo_dato":  "point",
                        "coordenadas": [{"lat":"-0.19713926299073917", "lon":"-78.49225762271467"}],
                        "distancia_min": 0,
                        "distancia_max":  20,
                        "zona_horaria": "una zona",
                        "estado_id": 1
                        },
                    update_data_fields= {"descripcion": "UISRAEL1", "zona_horaria":"Zona"},                    
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

@tag('views1')
class EmpleadoViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Empleado, serializer_class = EmpleadoSerializer,
                    reverse_name_detail = "api:empleado-detalle", 
                    reverse_name_list = "api:empleado",
                    serialized_data_object = {
                        "empresa_id": 1,
                        "cedula": '0600000001',
                        "nombres":  'Benjamin',
                        "apellidos": 'Nuevo Apellidos',
                        "foto": None,
                        "celular": '0999999999',
                        "departamento_id": 1,
                        "calendario_id": 1,
                        "estado_id": 1,
                        },
                    update_data_fields= {'apellidos': 'Cepeda',},                    
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

@tag('views')
class PerfilViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = Perfil, serializer_class = PerfilSerializer,
                    reverse_name_detail = "api:perfil-detalle", 
                    reverse_name_list = "api:perfil",
                    serialized_data_object = {
                        'descripcion': 'Nuevo Perfil',
                        'es_administrador': 1,
                        'estado_id':8,                        
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

@tag('views2')
class EmpleadoUbicacionViewTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp(object_class = EmpleadoUbicacion, serializer_class = EmpleadoUbicacionSerializer,
                    reverse_name_detail = "api:empleado-ubicacion-detalle", 
                    reverse_name_list = "api:empleado-ubicacion",
                    serialized_data_object = {
                        "empleado_id": 1,
                        "ubicacion_id": 2,
                        "estado_id": 1,                        
                        },
                    update_data_fields= {'ubicacion_id': 2,},
                    reverse_extra_param=True, 
                    filter_condition={"empleado__id":0},
                    parent_instance_class=Empleado
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

@tag('views2')
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
                    filter_condition={"empleado__empresa__id":0},
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

# c = CustomIniDataClass()
# c.init_data_test()