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
        
class TipoEventoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = TipoEvento
        fields = "__all__" 
                
class DepartamentoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = Departamento
        fields = "__all__"         

class UbicacionSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    
    class Meta:
        model = Ubicacion
        fields = ("__all__")
        
class EventoEmpleadoSerializer(serializers.ModelSerializer):
    evento = TipoEventoSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = EventoEmpleado
        fields = "__all__" 
                
class EmpleadoSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer(many=False, read_only=True)
    ubicacion = UbicacionSerializer(many=False, read_only=True)
    estado = EstadoSerializer(many=False, read_only=True)
    evento_empleado = EventoEmpleadoSerializer(many=False, read_only=True)

    class Meta:
        model = Empleado
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
        fields = "__all__"            

class CoordenadaSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(many=False, read_only=True)
    class Meta:
        model = Coordenada
        fields = ("__all__") 
        

        
        
    