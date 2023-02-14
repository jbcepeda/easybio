from django.shortcuts import render
from rest_framework.views import APIView
from api.models import *
from api.serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models.query_utils import Q

class EstadoDetalle(APIView):

    def get(self, request, id):
        try:
            local_instance = Estado.objects.get(id=id)
            if local_instance:
                serializer = EstadoSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)

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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Estado.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Estados(APIView):
    def get(self, request):
        local_instance = Estado.objects.all()
        serializer = EstadoSerializer(local_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EstadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetalle(APIView):

    def get(self, request, id):
        try:
            local_instance = Empresa.objects.get(id=id)
            if local_instance:
                serializer = EmpresaSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Empresa.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Empresas(APIView):
    def get(self, request):
        local_instance = Empresa.objects.all()
        serializer = EmpresaSerializer(local_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartamentoDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Departamento.objects.get(id=id)
            if local_instance:
                serializer = DepartamentoSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Departamento.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UbicacionDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Ubicacion.objects.get(id=id)
            if local_instance:
                print(type(local_instance))
                serializer = UbicacionSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Ubicacion.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
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
            print(ex.__dict__)
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        serializer = UbicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpleadoDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Empleado.objects.get(id=id)
            if local_instance:
                cur_lat = request.GET.get('la', None)
                cur_lon = request.GET.get('lo', None)
                if cur_lat is not None and cur_lon is not None:
                    print("la:{} lo:{}".format(cur_lat, cur_lon))
                    local_instance.lat_actual=cur_lat
                    local_instance.lon_actual=cur_lon
                    if local_instance.en_rango:
                        print("En rango")
                    else:
                        print("Fuera de rango")
                    print(local_instance.distancia_actual)
                serializer = EmpleadoSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
            print(ex.__dict__)
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Empleado.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerfilDetalle(APIView):
    def get(self, request, id):
        try:
            local_instance = Perfil.objects.get(id=id)
            if local_instance:
                serializer = PerfilSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Perfil.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Perfiles(APIView):
    def get(self, request):
        local_instance = Perfil.objects.all()
        serializer = PerfilSerializer(local_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetalle(APIView):

    def get(self, request, id):
        try:
            local_instance = Usuario.objects.get(id=id)
            if local_instance:
                serializer = UsuarioSerializer(local_instance)
                return Response(serializer.data)
        except Exception as ex:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            local_instance = Usuario.objects.get(pk=id)
            local_instance.delete()
            return Response(status.HTTP_200_OK)
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Usuarios(APIView):
    def get(self, request):
        parent_id = request.GET.get('parent_id', None)
        if parent_id is not None:
            local_instance = Usuario.objects.filter(Q(empleado__departamento__empresa__id=parent_id))
            serializer = UsuarioSerializer(local_instance, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)