
"""_summary_
    EasyBio API Model test
"""

import logging
from rest_framework.test import APITestCase
from api.models import * 
from api import customfunctions
from api.test.utils import CustomIniDataClass
logger = logging.getLogger(__name__)
class CustomFunctionsTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        return super().setUp()
    
    def test_valida_dentro_rango_punto(self):
        lat = -0.19044428987472398
        lon = -78.4882888957929
        tipo_dato = 'point'
        en_rango, distancia_actual = customfunctions.valida_rango(tipo_dato = tipo_dato, \
            coordenadas_ubicacion = self.ubicacion.coordenadas, distancia_max = self.ubicacion.distancia_max, \
                lat = lat, lon = lon)
        self.assertEqual(en_rango, True)

    def test_valida_fuera_rango_punto(self):
        lat = -0.1898208998328632 
        lon = -78.48750746006637
        tipo_dato = 'point'
        en_rango, distancia_actual = customfunctions.valida_rango(tipo_dato = tipo_dato, \
            coordenadas_ubicacion = self.ubicacion.coordenadas, distancia_max = self.ubicacion.distancia_max, \
                lat = lat, lon = lon)
        self.assertEqual(en_rango, False)
    
    def test_valida_dentro_rango_poligono(self):
        lat = -0.19726573944750136
        lon = -78.49225264151514
        self.ubicacion.tipo_dato = 'polygon'
        self.ubicacion.coordenadas = [
                {"lat":-0.19713926299073917, "lon":-78.49225762271467},
                {"lat":-0.1971883255734097, "lon":-78.49206137121821},
                {"lat":-0.19758857295292392, "lon":-78.49215949696644},
                {"lat":-0.19753434588915864, "lon":-78.49237382425862},
            ]
        en_rango, distancia_actual = customfunctions.valida_rango(tipo_dato = self.ubicacion.tipo_dato, \
            coordenadas_ubicacion = self.ubicacion.coordenadas, distancia_max = self.ubicacion.distancia_max, \
                lat = lat, lon = lon)
        self.assertEqual(en_rango, True)

    def test_valida_fuera_rango_poligono(self):
        lat = -0.19696485788987494 
        lon = -78.49190597157524
        self.ubicacion.coordenadas = [
                {"lat":-0.19713926299073917, "lon":-78.49225762271467},
                {"lat":-0.1971883255734097, "lon":-78.49206137121821},
                {"lat":-0.19758857295292392, "lon":-78.49215949696644},
                {"lat":-0.19753434588915864, "lon":-78.49237382425862},
            ]
      
        en_rango, distancia_actual = customfunctions.valida_rango(tipo_dato = self.ubicacion.tipo_dato, \
            coordenadas_ubicacion = self.ubicacion.coordenadas, distancia_max = self.ubicacion.distancia_max, \
                lat = lat, lon = lon)
        self.assertEqual(en_rango, False)
        
    def test_valida_rango_sin_coordenadas(self):
        self.ubicacion.coordenadas = None
        en_rango, distancia_actual = customfunctions.valida_rango(tipo_dato = self.ubicacion.tipo_dato, \
            coordenadas_ubicacion = self.ubicacion.coordenadas, distancia_max = self.ubicacion.distancia_max, \
                lat = None, lon = None)

    def test_valida_rango_no_valido_tipo_dato(self):
        lat = -0.19696485788987494 
        lon = -78.49190597157524
        en_rango, distancia_actual = customfunctions.valida_rango(tipo_dato = 'tipo_erroneo', \
            coordenadas_ubicacion = self.ubicacion.coordenadas, distancia_max = self.ubicacion.distancia_max, \
                lat = lat, lon = lon)
class EstadoModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.estado.__str__)
        return super().setUp()
    
    def test_estado_list(self):
        items_count = Estado.objects.filter(descripcion = "Inicial").count()
        self.assertEqual(items_count,1)
        
class EmpresaModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.empresa.__str__)
        return super().setUp()
    
    def test_empresa_list(self):
        items_count = Empresa.objects.filter(ruc = "1111111111111").count()
        self.assertEqual(items_count,1)
        
class TipoEventoModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.tipo_evento.__str__)
        return super().setUp()

    def test_tipo_evento_list(self):
        items_count = TipoEvento.objects.filter(empresa = self.empresa).count()
        self.assertEqual(items_count,1)
        
class DepartamentoModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.departamento.__str__)
        return super().setUp()

    def test_departamento_list(self):
        items_count = Departamento.objects.filter(empresa = self.empresa, descripcion = "Sistemas").count()
        self.assertEqual(items_count,1)
        
class UbicacionModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.ubicacion.__str__)
        return super().setUp()

    def test_ubicacion_list(self):
        items_count = Ubicacion.objects.filter(empresa = self.empresa, descripcion = "RPDMQ").count()
        self.assertEqual(items_count,1)
        
class EmpleadoModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.empleado.__str__)
        return super().setUp()

    def test_empleado_list(self):
        items_count = Empleado.objects.filter(departamento = self.departamento, apellidos = "Cepeda").count()
        self.assertEqual(items_count,1)
        
class PerfilModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.perfil.__str__)
        return super().setUp()

    def test_perfil_list(self):
        items_count = Perfil.objects.filter(descripcion = "Empleado").count()
        self.assertEqual(items_count,1)
        
class UsuarioModelTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        logger.debug(self.usuario.__str__)
        return super().setUp()

    def test_usuario_list(self):
        items_count = Usuario.objects.filter(nombre_usuario = "bcepeda").count()
        self.assertEqual(items_count,1)
        
class EventoEmpleadoTestCase(APITestCase, CustomIniDataClass):
    def setUp(self) -> None:
        self.init_data_test()
        return super().setUp()

    def test_evento_empleado_list(self):
        _coordenada = {"lat": -0.19044383946406043, "lon": -78.48829875522068}
        self.evento_empleado = EventoEmpleado.objects.create(   
            empleado = self.empleado, 
            evento = self.tipo_evento,
            fecha = '2023-02-17',
            hora = '08:30',
            coordenada_evento = _coordenada,
            intento_exitoso = False,
            distancia_actual = 0,
            dispositivo = 'TestCase',
            ubicacion = self.ubicacion,
            estado = self.estado
        )
        items_count = EventoEmpleado.objects.filter(dispositivo = "TestCase").count()
        logger.debug(self.evento_empleado.__str__)
        self.assertEqual(items_count,1)

    def test_evento_empleado_en_rango(self):
        _result = False
        _coordenada = {"lat": -0.19044383946406043, "lon": -78.48829875522068}
        self.evento_empleado = EventoEmpleado.objects.create(   
            empleado = self.empleado, 
            evento = self.tipo_evento,
            fecha = '2023-02-17',
            hora = '08:30',
            coordenada_evento = _coordenada,
            intento_exitoso = False,
            distancia_actual = 0,
            dispositivo = 'TestCase',
            ubicacion = self.ubicacion,
            estado = self.estado
        )
        _result = self.evento_empleado.en_rango()
        self.empleado.evento_empleado = self.evento_empleado
        self.assertEqual(_result and self.evento_empleado.intento_exitoso,True)

    def test_evento_empleado_fuera_de_rango(self):
        _result = False
        _coordenada = {"lat": -0.1898208998328632, "lon": -78.48750746006637}
        self.evento_empleado = EventoEmpleado.objects.create(   
            empleado = self.empleado, 
            evento = self.tipo_evento,
            fecha = '2023-02-17',
            hora = '08:30',
            coordenada_evento = _coordenada,
            intento_exitoso = False,
            distancia_actual = 0,
            dispositivo = 'TestCase',
            ubicacion = self.ubicacion,
            estado = self.estado
        )
        _result =self.evento_empleado.en_rango()
        logger.debug(self.evento_empleado.__str__)
        self.assertEqual(_result and self.evento_empleado.intento_exitoso, False)

    def test_evento_empleado_sin_coordenada(self):
        _result = False
        _coordenada = None
        self.evento_empleado = EventoEmpleado.objects.create(   
            empleado = self.empleado, 
            evento = self.tipo_evento,
            fecha = '2023-02-17',
            hora = '08:30',
            coordenada_evento = _coordenada,
            intento_exitoso = False,
            distancia_actual = 0,
            dispositivo = 'TestCase',
            ubicacion = self.ubicacion,
            estado = self.estado
        )
        _result =self.evento_empleado.en_rango()
        logger.debug(self.evento_empleado.__str__)
        self.assertEqual(_result and self.evento_empleado.intento_exitoso, False)

    def test_evento_empleado_mal_formato_coordenada(self):
        _result = False
        _coordenada = {"lat": "ABCD5", "lon": "XYZ2"}
        self.evento_empleado = EventoEmpleado.objects.create(   
            empleado = self.empleado, 
            evento = self.tipo_evento,
            fecha = '2023-02-17',
            hora = '08:30',
            coordenada_evento = _coordenada,
            intento_exitoso = False,
            distancia_actual = 0,
            dispositivo = 'TestCase',
            ubicacion = self.ubicacion,
            estado = self.estado
        )
        _result =self.evento_empleado.en_rango()
        logger.debug(self.evento_empleado.__str__)
        self.assertEqual(_result and self.evento_empleado.intento_exitoso, False)

