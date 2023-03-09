from rest_framework import serializers
from decimal import Decimal
from api.models import *

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"
        
class EmpresaSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = Empresa
        fields = "__all__"
        read_only_fields = (
            "codigo_asignado", )
        
class EmpresaGrupoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    class Meta:
        model = EmpresaGrupo
        fields = "__all__"

class DepartamentoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = Departamento
        fields = "__all__"         

class FeriadoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)

    class Meta:
        model = Feriado
        fields = "__all__" 
                
class CalendarioSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)

    class Meta:
        model = Calendario
        fields = "__all__" 

class DiaSerializer(serializers.ModelSerializer):
    calendario = CalendarioSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)

    class Meta:
        model = Dia
        fields = "__all__" 

class FranjaTiempoSerializer(serializers.ModelSerializer):
    calendario = CalendarioSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)

    class Meta:
        model = FranjaTiempo
        fields = "__all__" 

class DiaFranjaTiempoSerializer(serializers.ModelSerializer):
    dia = DiaSerializer(many=False, read_only=True)
    franja_tiempo = FranjaTiempoSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)

    class Meta:
        model = DiaFranjaTiempo
        fields = "__all__" 

class UbicacionSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    
    class Meta:
        model = Ubicacion
        fields = ("__all__")
        
class EmpleadoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    departamento = DepartamentoSerializer(many=False, read_only=True)
    calendario = CalendarioSerializer(many=True, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)

    class Meta:
        model = Empleado
        fields = "__all__"    

class EmpleadoUbicacionSerializer(serializers.ModelSerializer):
    empleado = EmpleadoSerializer(many=False, read_only=True)
    ubicacion = UbicacionSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)

    class Meta:
        model = EmpleadoUbicacion
        fields = "__all__"    
                        
                        
class PerfilSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = Perfil
        fields = "__all__"        

class UsuarioSerializer(serializers.ModelSerializer):
    empleado = EmpleadoSerializer(many=False, read_only=True)
    perfil = PerfilSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = Usuario
        fields = ("__all__") 
        
    # def save(self, **kwargs):
    #     logger.debug("UsuarioSerializer - CREATE")
    #     self.clave = make_password(self.clave)
    #     return super().save(**kwargs)
        

class CoordenadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenada
        fields = ("__all__") 
        
class EventoEmpleadoSerializer(serializers.ModelSerializer):
    empleado = EmpleadoSerializer(many=False, read_only=True)
    dia_franja_tiempo = DiaFranjaTiempoSerializer(many=False, read_only=True)
    ubicacion = UbicacionSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = EventoEmpleado
        fields = "__all__" 

        
        
    