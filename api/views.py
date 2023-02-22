from django.shortcuts import render
from rest_framework.views import APIView
from api.models import *
from api.serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query_utils import Q
import logging

logger = logging.getLogger(__name__)

class EstadoDetalle(APIView):

    def get(self, request, id):
        try:
            local_instance = Estado.objects.get(id=id)
            if local_instance:
                serializer = EstadoSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            local_instance = Estado.objects.get(pk=id)
            if local_instance:
                serializer = EstadoSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Estado.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Estados(APIView):
    def get(self, request):
        try:
            local_instance = Estado.objects.all()
            serializer = EstadoSerializer(local_instance, many=True)
            return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = EstadoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EmpresaDetalle(APIView):

    def get(self, request, id):
        try:
            local_instance = Empresa.objects.get(id=id)
            if local_instance:
                serializer = EmpresaSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            local_instance = Empresa.objects.get(pk=id)
            if local_instance:
                serializer = EmpresaSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Empresa.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Empresas(APIView):
    def get(self, request):
        try:
            local_instance = Empresa.objects.all()
            serializer = EmpresaSerializer(local_instance, many=True)
            return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = EmpresaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)    

class TipoEventoDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = TipoEvento.objects.get(id=id)
            if local_instance:
                serializer = TipoEventoSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            local_instance = TipoEvento.objects.get(pk=id)
            if local_instance:
                serializer = TipoEventoSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = TipoEvento.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

class TipoEventos(APIView):
    def get(self, request):
        try:
            parent_id = request.GET.get('parent_id', None)
            if parent_id is not None:
                local_instance = TipoEvento.objects.filter(Q(empleado__id=parent_id))
                serializer = TipoEventoSerializer(local_instance, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)    
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        try:
            serializer = TipoEventoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DepartamentoDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Departamento.objects.get(id=id)
            if local_instance:
                serializer = DepartamentoSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            local_instance = Departamento.objects.get(pk=id)
            if local_instance:
                serializer = DepartamentoSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Departamento.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Departamentos(APIView):
    def get(self, request):
        try:
            parent_id = request.GET.get('parent_id', None)
            if parent_id is not None:
                local_instance = Departamento.objects.filter(Q(empresa__id=parent_id))
                serializer = DepartamentoSerializer(local_instance, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)    
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        try:
            serializer = DepartamentoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UbicacionDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Ubicacion.objects.get(id=id)
            if local_instance:
                serializer = UbicacionSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            local_instance = Ubicacion.objects.get(pk=id)
            if local_instance:
                serializer = UbicacionSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Ubicacion.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Ubicaciones(APIView):
    def get(self, request):
        try:
            parent_id = request.GET.get('parent_id', None)
            if parent_id is not None:
                local_instance = Ubicacion.objects.filter(Q(empresa__id=parent_id))
                #local_instance = Ubicacion.objects.all()               
                serializer = UbicacionSerializer(local_instance, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)    
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        try:
            serializer = UbicacionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

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
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            local_instance = Empleado.objects.get(pk=id)
            if local_instance:
                serializer = EmpleadoSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Empleado.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Empleados(APIView):
    def get(self, request):
        try:
            parent_id = request.GET.get('parent_id', None)
            if parent_id is not None:
                local_instance = Empleado.objects.filter(Q(departamento__empresa__id=parent_id))
                serializer = EmpleadoSerializer(local_instance, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)    
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        try:
            serializer = EmpleadoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class PerfilDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Perfil.objects.get(id=id)
            if local_instance:
                serializer = PerfilSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            local_instance = Perfil.objects.get(pk=id)
            if local_instance:
                serializer = PerfilSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Perfil.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Perfiles(APIView):
    def get(self, request):
        try:
            local_instance = Perfil.objects.all()
            serializer = PerfilSerializer(local_instance, many=True)
            return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = PerfilSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UsuarioDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Usuario.objects.get(id=id)
            if local_instance:
                serializer = UsuarioSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

    def put(self, request, id):
        try:
            local_instance = Usuario.objects.get(pk=id)
            if local_instance:
                serializer = UsuarioSerializer(local_instance, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Usuario.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Usuarios(APIView):
    def get(self, request):
        try:
            parent_id = request.GET.get('parent_id', None)
            if parent_id is not None:
                local_instance = Usuario.objects.filter(Q(empleado__departamento__empresa__id=parent_id))
                serializer = UsuarioSerializer(local_instance, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)    
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = UsuarioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(str(ex))
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        
def error400View(request, exception):
    return render(request, 'error_404.html', status = 400)

def error403View(request, exception):
    return render(request, 'error_404.html', status = 403)

def error404View(request, exception):
    return render(request, 'error_404.html', status = 404)

def error500View(request):
    return render(request, 'error_404.html', status = 500)