from django.shortcuts import render
from rest_framework.views import APIView
from api.models import *
from api.serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query_utils import Q
import logging

logger = logging.getLogger(__name__)

class GenericObjectDetail(APIView):
    def __init__(self, object_class, serializer_class):
        self.object_class = object_class
        self.serializer_class = serializer_class
        super().__init__()

    def get(self, request, id):
        try:
            local_instance = self.object_class.objects.get(id=id)
            if local_instance:
                serializer = self.serializer_class(local_instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            local_instance = self.object_class.objects.get(pk=id)
            if local_instance:
                serializer = self.serializer_class(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = self.object_class.objects.get(pk=id)
            local_instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GenericObjects(APIView):
    def __init__(self, object_class, serializer_class, kwargs):
        self.object_class = object_class
        self.serializer_class = serializer_class 
        self._kwargs = kwargs

    def get(self, request):
        try:
            parent_id = request.GET.get('parent_id', None)
            if self._kwargs is not None:
                if parent_id is not None:
                    self._kwargs.update({list(self._kwargs.keys())[0]: parent_id})
                    local_instance = self.object_class.objects.filter(Q(**self._kwargs))
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                local_instance = self.object_class.objects.all()
            serializer = self.serializer_class(local_instance, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class EstadoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Estado, EstadoSerializer)

class Estados(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Estado, serializer_class=EstadoSerializer, kwargs=None)

class EmpresaDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Empresa, EmpresaSerializer)

class Empresas(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Empresa, serializer_class=EmpresaSerializer, kwargs=None)
  
class TipoEventoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(object_class=TipoEvento, serializer_class=TipoEventoSerializer)

class TipoEventos(GenericObjects):
    def __init__(self):
        super().__init__(object_class=TipoEvento, serializer_class=TipoEventoSerializer, kwargs={'empresa__id':0})

class DepartamentoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Departamento, DepartamentoSerializer)

class Departamentos(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Departamento, serializer_class = DepartamentoSerializer,
                          kwargs={'empresa__id':0})

class UbicacionDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Departamento, DepartamentoSerializer)

class Ubicaciones(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Ubicacion, serializer_class = UbicacionSerializer,
                          kwargs={'empresa__id':0})
        
class PerfilDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Perfil, PerfilSerializer)

class Perfiles(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Perfil, serializer_class = PerfilSerializer,
                          kwargs=None)
        
class UsuarioDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Usuario, UsuarioSerializer)
                        
class Usuarios(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Usuario, serializer_class = UsuarioSerializer,
                          kwargs={'empleado__ubicacion__empresa__id':0})

class EmpleadoDetalle(APIView):
    def get(self, request, id):
        try:
            _data = request.data
            _validacion_en_rango = False
            local_instance = Empleado.objects.get(id=id)
            if local_instance:
                if _data is not None and _data.evento_empleado is not None and \
                    _data.evento_empleado_coordenadas is not None:
                    local_instance.evento_empleado = _data.evento_empleado
                    _validacion_en_rango = local_instance.evento_empleado.en_rango() 
                    if local_instance.evento_empleado.exitoso:
                        logger.debug("En rango")
                    else:
                        logger.debug("Fuera de rango:")
                    logger.debug(local_instance.evento_empleado.__str__)
                    serializer = EventoEmpleadoSerializer(local_instance.evento_empleado)
                    if serializer.is_valid():
                        serializer.save()                        
                serializer = EmpleadoSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            local_instance = Empleado.objects.get(pk=id)
            if local_instance:
                serializer = EmpleadoSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Empleado.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Empleados(APIView):
    def get(self, request):
        try:
            parent_id = request.GET.get('parent_id', None)
            if parent_id is not None:
                local_instance = Empleado.objects.filter(Q(departamento__empresa__id=parent_id))
                serializer = EmpleadoSerializer(local_instance, many=True)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        try:
            serializer = EmpleadoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)        
        
def error400View(request, exception):
    return render(request, 'error_404.html', status = 400)

def error403View(request, exception):
    return render(request, 'error_404.html', status = 403)

def error404View(request, exception):
    return render(request, 'error_404.html', status = 404)

def error500View(request):
    return render(request, 'error_404.html', status = 500)