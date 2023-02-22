from djongo import models
from decimal import Decimal
from api import customfunctions as cf

class Estado(models.Model):
    descripcion = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    def __str__(self):
        return "%s %s" % (self.descripcion, self.color)
        
class Empresa(models.Model):
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
    
    def __str__(self):
        return "%s %s" % (self.ruc, self.razon_social)

class TipoEvento(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.RESTRICT,
        related_name='tipo_evento_empresa',
    )
    descripcion = models.CharField(max_length=100)
    orden = models.SmallIntegerField(default=0)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='tipo_evento_estado')
    def __str__(self):
        return "%s %s %s %s" % (self.empresa, self.descripcion, self.orden, self.estado)
        
class Departamento(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.RESTRICT,
        related_name='departamento_empresa',
    )
    descripcion = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='departamento_estado')

        
    def __str__(self):
        return "%s %s" % (self.empresa.ruc, self.descripcion)

class Coordenada(models.Model):
    lat = models.CharField(max_length = 20, default = "0.0")
    lon = models.CharField(max_length = 20, default = "0.0")
    class Meta:
        abstract = True
    
    def __str__(self):
        return "Coordenada"

# class CoordenadaForm(forms.ModelForm):
#     class Meta:
#         model = Coordenada
#         fields = (
#             'lat', 'lon'
#         )
  
        
class Ubicacion(models.Model):
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
 
    def __str__(self):
         return "%s %s %s %s %s %s" % (self.empresa.ruc,self.descripcion,
                              self.tipo_dato.__str__, self.coordenadas, self.distancia_min, self.distancia_max)  
        
class Empleado(models.Model):
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
    @property
    def evento_empleado(self) -> any:
        return self._evento_empleado
    
    @evento_empleado.setter
    def evento_empleado(self, value)-> None:
        self._evento_empleado = value
      
    def __str__(self):
        return "%s %s %s %s %s" % (self.departamento.empresa.ruc, 
                             self.departamento.descripcion,
                             self.nombres, self.apellidos, self.ubicacion.coordenadas)    

class Perfil(models.Model):
    descripcion = models.CharField(max_length=20)
    es_administrador = models.SmallIntegerField(default=0)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='perfil_estado')
    
    def __str__(self):
        return "%s" % (self.descripcion)


class Usuario(models.Model):
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
    
    def __str__(self):
        return "%s %s" % (self.nombre_usuario, 
                             self.empleado.departamento.empresa.id)
    

class EventoEmpleado(models.Model):
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.RESTRICT,
        related_name='evento_empleado_empleado',
    )
    evento = models.ForeignKey(TipoEvento, on_delete=models.RESTRICT, null=False,
                               related_name='evento_empleado_tipo_evento')
    fecha = models.DateField()
    hora = models.TimeField()
    coordenada_evento = models.Field(Coordenada())
    distancia_actual = models.IntegerField()
    dispositivo = models.CharField(max_length=20, null=False)
    ubicacion = models.ForeignKey(Ubicacion, on_delete = models.RESTRICT, null = False,
                                 related_name = 'evento_empleado_ubicacion')
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='evento_empleado_estado')
    @property
    def en_rango(self)->bool:
        self._en_rango = False
        self.distancia_actual = 0
        try:
            if not self.coordenada_evento:
                return self._en_rango
            self._en_rango, self.distancia_actual = cf.valida_rango( 
                tipo_dato = self.ubicacion.tipo_dato, 
                coordenadas_ubicacion = self.ubicacion.coordenadas,
                distancia_max = self.ubicacion.distancia_max,
                lat = Decimal(self.coordenada_evento["lat"]), 
                lon = Decimal(self.coordenada_evento["lon"])) 
        except Exception as ex:
            print(str(ex))
            return False
        finally:
            return  self._en_rango and self.distancia_actual <= self.ubicacion.distancia_max
        
    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (
            self.empleado, self.evento, self.fecha, self.hora, self.coordenada_evento, self.dispositivo,
            self.ubicacion, self.estado)
