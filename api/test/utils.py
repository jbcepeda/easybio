from api.models import *
from datetime import datetime, time
import hashlib
from decouple import config
from api.auth_features.util import ApiCrypto
import json

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
            meses_disponible_datos= 3,
            permitir_uso_varios_dispositivos = False
            )


        self.departamento = Departamento.objects.create(
            empresa = self.empresa,
            descripcion = "Sistemas",
            estado = self.estado
        )

        self.feriado = Feriado.objects.create(
            empresa = self.empresa,
            fecha = "2023-05-01",
            descripcion = "Dia del trabajo",
            es_global = True,
            estado = self.estado
        )
        
        self.calendario = Calendario.objects.create(
            empresa = self.empresa,
            nombre='jornada normal',
            descripcion='Jornada semanal L-V 9AM-5PM',
            estado = self.estado
        )

        self.dia = Dia.objects.create(calendario = self.calendario, dia_semana = 1, estado = self.estado)
        self.dia = Dia.objects.create(calendario = self.calendario, dia_semana = 2, estado = self.estado)
        self.dia = Dia.objects.create(calendario = self.calendario, dia_semana = 3, estado = self.estado)
        self.dia = Dia.objects.create(calendario = self.calendario, dia_semana = 4, estado = self.estado)
        self.dia = Dia.objects.create(calendario = self.calendario, dia_semana = 5, estado = self.estado)

        self.franja_tiempo = FranjaTiempo.objects.create(
            calendario = self.calendario,
            descripcion = 'Horario normal trabajo 9AM a 5PM',
            es_laborable = True,
            tiene_horario_fijo = True,
            duracion_minutos = 0,
            hora_inicio = '09:00',
            hora_fin = '18:00',
            estado = self.estado
        )
        
        self.dia_franja_tiempo = DiaFranjaTiempo.objects.create(
            dia = self.dia,
            franja_tiempo = self.franja_tiempo,
            estado = self.estado
        )        
        
        self.ubicacion = Ubicacion.objects.create(
            empresa = self.empresa,
            descripcion = "RPDMQ",
            tipo_dato =  "point",
            coordenadas = [{"lat":-0.19041117621469852, "lon":-78.48837800323963}],
            distancia_min =  0,
            distancia_max =  20,
            zona_horaria = "Zona default",
            estado = self.estado
        )
         
        self.ubicacion = Ubicacion.objects.create(
            empresa = self.empresa,
            descripcion = "Uisrael",
            tipo_dato =  "point",
            coordenadas = [{"lat":"-0.19713926299073917", "lon":"-78.49225762271467"}],
            distancia_min =  0,
            distancia_max =  20,
            zona_horaria = "-5 GTM",
            estado = self.estado
        )        
        
        self.empleado = Empleado.objects.create(
            empresa = self.empresa,
            cedula = '0600000000',
            nombres = 'Benjamin',
            apellidos = 'Cepeda',
            foto = None,
            celular = '0999999999',
            departamento = self.departamento,
            calendario = self.calendario,
            estado = self.estado
        )
        
        self.empleado_ubicacion = EmpleadoUbicacion.objects.create(
            empleado = self.empleado,
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
    
    def init_general_mobile_token(utc_datetime):
        if utc_datetime:
            _d = str(utc_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
        else:
            _d = str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
        s= config('BASE_KEY', cast=str)
        _general_mobile_key=config('GENERAL_MOBILE_KEY', cast=str)
        _base_string = _general_mobile_key + _d
        _t = hashlib.sha256(_base_string.encode('utf-8')).hexdigest()
        _d = ApiCrypto.encrypt(s=s, m=_d)       
        _data=json.dumps({
            't': _t,
            'd': _d,
        })
        # logger.debug("init_general_mobile_token _data:{} ".format(str(_data)))
        return ApiCrypto.encrypt(s=s, m=_data)
        

