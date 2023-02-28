from api.models import *
from datetime import datetime
import hashlib


class CustomIniDataClass(object):

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
            estado = self.estado,
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

class CustomIniDataToken(object):
    
    def init_general_mobile_token():
        _general_mobile_token='f67316be-db7d-4b43-aae1-7954f76d9939'
        _dt = datetime.utcnow()
        _str_dt = str(_dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
        _base_string = _general_mobile_token + _str_dt
        _t = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()
        logger.debug("BASE_STRING: {}".format(_base_string))
        _data={
            't': _t,
            'dt': _str_dt,
        }        
        return _data
        

