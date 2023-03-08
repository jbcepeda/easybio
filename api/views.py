from django.shortcuts import render
from rest_framework.views import APIView
from api.models import *
from api.serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query_utils import Q
import logging
from api.token_features.authorization import *
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
                logger.debug("SERIALIZE ERRORS {}".format(serializer.errors))
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
            if request and len(request.data)>0 and serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            logger.debug("SERIALIZE ERRORS {}".format(serializer.errors))
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # TODO 
    # SOLUCIONAR problema (N+1)
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.prefetch_related(
    #         Prefetch('cities')
    #     )
    #     return queryset    
    
    
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
class EmpresaGrupoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(EmpresaGrupo, EmpresaGrupoSerializer)

class EmpresaGrupos(GenericObjects):
    def __init__(self):
        super().__init__(object_class=EmpresaGrupo, serializer_class=EmpresaGrupoSerializer, kwargs=None)

class DepartamentoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Departamento, DepartamentoSerializer)

class Departamentos(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Departamento, serializer_class = DepartamentoSerializer,
                          kwargs={'empresa__id':0})

class FeriadoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Feriado, FeriadoSerializer)

class Feriados(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Feriado, serializer_class = FeriadoSerializer,
                          kwargs={'empresa__id':0})

class CalendarioDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Calendario, CalendarioSerializer)

class Calendarios(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Calendario, serializer_class = CalendarioSerializer,
                          kwargs={'empresa__id':0})

class DiaDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Dia, DiaSerializer)

class Dias(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Dia, serializer_class = DiaSerializer,
                          kwargs={'calendario__id':0})
        
class FranjaTiempoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(FranjaTiempo, FranjaTiempoSerializer)

class FranjaTiempos(GenericObjects):
    def __init__(self):
        super().__init__(object_class=FranjaTiempo, serializer_class = FranjaTiempoSerializer,
                          kwargs={'calendario__id':0})
        
class DiaFranjaTiempoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(DiaFranjaTiempo, DiaFranjaTiempoSerializer)

class DiaFranjaTiempos(GenericObjects):
    def __init__(self):
        super().__init__(object_class=DiaFranjaTiempo, serializer_class = DiaFranjaTiempoSerializer,
                          kwargs={'franja_tiempo__id':0})

class UbicacionDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Ubicacion, UbicacionSerializer)

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
        
class EmpleadoDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(Empleado, EmpleadoSerializer)
                        
class Empleados(GenericObjects):
    def __init__(self):
        super().__init__(object_class=Empleado, serializer_class = EmpleadoSerializer,
                          kwargs={'empresa__id':0})
        
class EmpleadoUbicacionDetalle(GenericObjectDetail):
    def __init__(self):
        super().__init__(EmpleadoUbicacion, EmpleadoUbicacionSerializer)
                        
class EmpleadoUbicaciones(GenericObjects):
    def __init__(self):
        super().__init__(object_class=EmpleadoUbicacion, serializer_class = EmpleadoUbicacionSerializer,
                          kwargs={'empleado__id':0})
class LoginAppView(APIView):
    def post(self, request):
        try:
            return Response(status = status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class GeneralTokenView(APIView):
    def post(self, request):
        try:
            _t = self.request.data.get('t')
            _d = self.request.data.get('d')
            if _t and _d:
                _v, _d = GeneralTokenAutorization.validate(t=_t, d=_d) 
                if _v:
                    return Response( data={'d':_d},status = status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex), extra={'className': self.__class__.__name__})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
def error400View(request, exception):
    return render(request, 'error_404.html', status = 400)

def error403View(request, exception):
    return render(request, 'error_404.html', status = 403)

def error404View(request, exception):
    return render(request, 'error_404.html', status = 404)

def error500View(request):
    return render(request, 'error_404.html', status = 500)