import logging
from djongo import models
from decimal import Decimal
from api import custom_functions as cf
import uuid
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxValueValidator, MinValueValidator

logger = logging.getLogger(__name__)

class CustomModel(object):
    def __str__(self):
        return str({f'{k}': f'{v}' for k, v in filter(
            lambda item: not item[0].startswith('_'),
            self.__dict__.items()
        )})


class Estado(CustomModel, models.Model):
    descripcion = models.CharField(max_length=50, null=False, unique=True)
    color = models.CharField(max_length=7)


class Empresa(CustomModel, models.Model):
    ruc = models.CharField(max_length=20, unique=True)
    razon_social = models.CharField(max_length=200, null=False)
    nombre_comercial = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200, null=False)
    telefono = models.CharField(max_length=14, null=False)
    nombres_contacto = models.CharField(max_length=100, null=False)
    cargo_contacto = models.CharField(max_length=50, null=False)
    email_contacto = models.EmailField(null=False)
    telefono_contacto = models.CharField(max_length=14, null=False)
    inicio_contrato = models.DateField(null=False)
    fin_contrato = models.DateField(null=False)
    codigo_asignado = models.UUIDField(default=uuid.uuid4, editable=False)
    meses_disponible_datos = models.SmallIntegerField()
    permitir_uso_varios_dispositivos = models.BooleanField()
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='empresa_estado')


class EmpresaGrupo(CustomModel, models.Model):
    empresa = models.OneToOneField(
        Empresa, on_delete=models.RESTRICT, null=False,
        primary_key=True,)
    grupo = models.ForeignKey(
        Empresa, on_delete=models.RESTRICT,
        related_name='empresa_grupo_grupo',)


class Departamento(CustomModel, models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.RESTRICT,
        related_name='departamento_empresa',
    )
    descripcion = models.CharField(max_length=100, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='departamento_estado')

    class Meta:
        unique_together = ("empresa", "descripcion")


class Feriado(CustomModel, models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.RESTRICT,
        related_name='feriado_empresa',
    )
    fecha = models.DateField(null=False)
    descripcion = models.CharField(max_length=50, null=False)
    es_global = models.BooleanField()
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='feriado_estado')

    class Meta:
        unique_together = ("empresa", "fecha")


class Calendario(CustomModel, models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.RESTRICT,
        related_name='calendario_empresa',
    )
    nombre = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='calendario_estado')

    class Meta:
        unique_together = ("empresa", "nombre")


class Dia(models.Model):
    calendario = models.ForeignKey(
        Calendario, on_delete=models.RESTRICT, null=False,
        related_name='dia_calendario',
    )
    dia_semana = models.SmallIntegerField(
        null=False,
        validators=[MaxValueValidator(7), MinValueValidator(1)]
    )
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='dia_estado')

    class Meta:
        unique_together = ("calendario", "dia_semana")


class FranjaTiempo(CustomModel, models.Model):
    calendario = models.ForeignKey(
        Calendario, on_delete=models.RESTRICT,
        related_name='franja_tiempo_calendario',
    )
    descripcion = models.CharField(max_length=50, null=False)
    es_laborable = models.BooleanField()
    # Se aplica al calendario
    # Inicia siempre a la misma hora
    # Finaliza siempre a la misma hora
    tiene_horario_fijo = models.BooleanField()
    # "tiene_horario_fijo = False"
    # Tiene una duración en minutos fijo
    # Y puede tomarse dentro de un rango de horario
    # Ej: Almuerzo dura 1 hora entre las 12:00 y las 14:00
    duracion_minutos = models.SmallIntegerField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='franja_tiempo_estado')

    class Meta:
        unique_together = ("calendario", "descripcion")


class DiaFranjaTiempo(CustomModel, models.Model):
    dia = models.ForeignKey(
        Dia, on_delete=models.RESTRICT,
        related_name='dia_franja_tiempo_dia'
    )
    franja_tiempo = models.ForeignKey(
        FranjaTiempo, on_delete=models.RESTRICT,
        related_name='dia_franja_tiempo_franja_tiempo'
    )
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='dia_franja_tiempo_estado')

    class Meta:
        unique_together = ("dia", "franja_tiempo")


class Coordenada(models.Model):
    lat = models.CharField(max_length=20, default="0.0")
    lon = models.CharField(max_length=20, default="0.0")

    class Meta:
        abstract = True


class Ubicacion(CustomModel, models.Model):
    # TIPOS = (('point','point'), ('polygon','polygon'))
    empresa = models.ForeignKey(
        Empresa, on_delete=models.RESTRICT,
        related_name='ubicacion_empresa',
    )
    descripcion = models.CharField(max_length=100, null=False)
    tipo_dato = models.CharField(max_length=10, default='point')
    coordenadas = models.ArrayField(model_container=Coordenada, null=False)
    distancia_min = models.IntegerField(default=0)
    distancia_max = models.IntegerField(default=50)
    zona_horaria = models.CharField(max_length=50, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='ubicacion_estado')


class Empleado(CustomModel, models.Model):
    empresa = models.ForeignKey(
        Empresa, on_delete=models.RESTRICT,
        related_name='empleado_empresa',
    )
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    foto = models.TextField(null=True)
    celular = models.CharField(max_length=14)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.RESTRICT,
        related_name='empleado_departamento',
    )
    calendario = models.ForeignKey(Calendario, on_delete=models.RESTRICT,
                                   related_name='empleado_calendario')
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='empleado_estado')

    class Meta:
        unique_together = ("empresa", "cedula")


class EmpleadoUbicacion(CustomModel, models.Model):
    empleado = models.ForeignKey(
        Empleado, on_delete=models.RESTRICT,
        related_name='empleado_ubicacion_empleado',
    )
    ubicacion = models.ForeignKey(
        Ubicacion, on_delete=models.RESTRICT,
        related_name='empleado_ubicacion_ubicacion',
    )
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='empleado_ubicacion_estado')

    class Meta:
        unique_together = ("empleado", "ubicacion")


class Perfil(CustomModel, models.Model):
    descripcion = models.CharField(max_length=20)
    es_administrador = models.SmallIntegerField(default=0)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='perfil_estado')


class Usuario(CustomModel, models.Model):
    nombre_usuario = models.CharField(max_length=20, unique=True)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.RESTRICT,
        related_name='usuario_empleado',
    )
    clave = models.CharField(max_length=20, null=False)
    perfil = models.ForeignKey(Perfil, on_delete=models.RESTRICT,
                               related_name='usuario_pefil')
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='usuario_estado')

    def save(self, *args, **kwargs):
        self.clave = make_password(self.clave)
        super(Usuario, self).save(*args, **kwargs)


class EventoEmpleado(CustomModel, models.Model):
    empleado = models.ForeignKey(
        Empleado, on_delete=models.RESTRICT,
        related_name='evento_empleado_empleado',
    )
    dia_franja_tiempo = models.ForeignKey(DiaFranjaTiempo, on_delete=models.RESTRICT,
                                          related_name='evento_empleado_dia_franja_tiempo')
    es_inicio = models.BooleanField(default=True)
    fecha = models.DateField()
    hora = models.TimeField()
    coordenada_evento = models.Field(Coordenada)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.RESTRICT,
                                  related_name='evento_empleado_ubicacion')
    # Distancia mts a la cual se realizó el evento
    distancia_actual = models.IntegerField(default=0)
    # Cumple con las condiciones de la Ubicacion asignada?
    cumple_ubicacion = models.BooleanField(default=False)
    dispositivo = models.CharField(max_length=20, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT,
                               related_name='evento_empleado_estado')

    def en_rango(self) -> bool:
        self.intento_exitoso = False
        self.distancia_actual = 0
        try:
            if not self.coordenada_evento:
                return self.intento_exitoso
            self.intento_exitoso, self.distancia_actual = cf.valida_rango(
                tipo_dato=self.ubicacion.tipo_dato,
                coordenadas_ubicacion=self.ubicacion.coordenadas,
                distancia_max=self.ubicacion.distancia_max,
                lat=Decimal(self.coordenada_evento["lat"]),
                lon=Decimal(self.coordenada_evento["lon"]))
        except Exception as ex:
            logger.error(str(ex))
            return False
        finally:
            return self.intento_exitoso and self.distancia_actual <= self.ubicacion.distancia_max
