from djongo import models


class Estado(models.Model):
    descripcion = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    
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

class Ubicacion(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.RESTRICT,
        related_name='ubicacion_empresa',
    )
    descripcion = models.CharField(max_length=100)
    coordenadas = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, null=False,
                                 related_name='ubicacion_estado')
    
    def __str__(self):
        return "%s %s %s" % (self.empresa.ruc,self.descripcion,
                             self.coordenadas) 
        
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
                             self.empresa.ruc)
    