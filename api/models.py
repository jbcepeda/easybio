import logging
from djongo import models
from decimal import Decimal
from api import customfunctions as cf

logger = logging.getLogger(__name__)

class CustomModel(object):
    def __str__(self):
        return str({f'{k}': f'{v}' for k, v in filter(
            lambda item: not item[0].startswith('_'),
                self.__dict__.items()
        )})

class Estado(CustomModel, models.Model):
    descripcion = models.CharField(max_length=50, null=False )
    color = models.CharField(max_length=7)
        
class Empresa(CustomModel, models.Model):
    ruc = models.CharField(max_length=13, unique=True)
    razon_social = models.CharField(max_length=200)
    nombre_comercial = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=14)
    nombres_contacto = models.CharField(max_length=100)
    cargo_contacto = models.CharField(max_length=50)
    email_contacto = models.EmailField()
    telefono_contacto = models.CharField(max_length=14)
    inicio_contrato = models.DateField()
    fin_contrato = models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='empresa_estado')
    

class TipoEvento(CustomModel, models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.RESTRICT,
        related_name='tipo_evento_empresa',
    )
    descripcion = models.CharField(max_length=100)
    orden = models.SmallIntegerField(default=0)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='tipo_evento_estado')
        
class Departamento(CustomModel, models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.RESTRICT,
        related_name='departamento_empresa',
    )
    descripcion = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='departamento_estado')

class Coordenada(models.Model):
    lat = models.CharField(max_length = 20, default = "0.0")
    lon = models.CharField(max_length = 20, default = "0.0")
    class Meta:
        abstract = True 
        
class Ubicacion(CustomModel, models.Model):
    #TIPOS = (('point','point'), ('polygon','polygon'))
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.RESTRICT,
        related_name='ubicacion_empresa',
    )
    descripcion = models.CharField(max_length = 100)
    tipo_dato = models.CharField(max_length = 10, default = 'point')
    coordenadas = models.ArrayField(model_container=Coordenada)
    distancia_min = models.IntegerField(default = 0)
    distancia_max =  models.IntegerField(default = 50)
    estado = models.ForeignKey(Estado, on_delete = models.RESTRICT, null = False,
                                 related_name = 'ubicacion_estado')
class Empleado(CustomModel, models.Model):
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    foto = models.TextField(null=True)
    celular = models.CharField(max_length=14)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.RESTRICT,
        related_name='empleado_departamento',
    )
    ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.RESTRICT,
        related_name='empleado_ubicacion',
    )
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='empleado_estado')
class Perfil(CustomModel, models.Model):
    descripcion = models.CharField(max_length=20)
    es_administrador = models.SmallIntegerField(default=0)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='perfil_estado')
    
class Usuario(CustomModel, models.Model):
    nombre_usuario=models.CharField(max_length=20, unique=True)
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.RESTRICT,
        related_name='usuario_empleado',
    )
    clave = models.CharField(max_length=15)
    perfil = models.ForeignKey(Perfil, on_delete=models.RESTRICT,
                                 related_name='usuario_pefil')
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='usuario_estado')
    
class EventoEmpleado(CustomModel, models.Model):
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.RESTRICT,
        related_name='evento_empleado_empleado',
    )
    evento = models.ForeignKey(TipoEvento, on_delete=models.RESTRICT, null=False,
                               related_name='evento_empleado_tipo_evento')
    fecha = models.DateField()
    hora = models.TimeField()
    coordenada_evento = models.Field(Coordenada)
    distancia_actual = models.IntegerField()
    intento_exitoso = models.BooleanField(default=False)
    dispositivo = models.CharField(max_length=20, null=False)
    ubicacion = models.ForeignKey(Ubicacion, on_delete = models.RESTRICT, null = False,
                                 related_name = 'evento_empleado_ubicacion')
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='evento_empleado_estado')
    def en_rango(self)->bool:
        self.intento_exitoso = False
        self.distancia_actual = 0
        try:
            if not self.coordenada_evento:
                return self.intento_exitoso
            self.intento_exitoso, self.distancia_actual = cf.valida_rango( 
                tipo_dato = self.ubicacion.tipo_dato, 
                coordenadas_ubicacion = self.ubicacion.coordenadas,
                distancia_max = self.ubicacion.distancia_max,
                lat = Decimal(self.coordenada_evento["lat"]), 
                lon = Decimal(self.coordenada_evento["lon"])) 
        except Exception as ex:
            logger.error(str(ex))
            return False
        finally:
            return  self.intento_exitoso and self.distancia_actual <= self.ubicacion.distancia_max
        