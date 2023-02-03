
from django.urls import path, include
from . import views
urlpatterns = [
    path('estado/<id>/', views.EstadoDetalle.as_view()),
    path('estado/', views.Estados.as_view()),
    path('empresa/<id>/', views.EmpresaDetalle.as_view()),
    path('empresa/', views.Empresas.as_view()),
    path('departamento/<id>/', views.DepartamentoDetalle.as_view()),
    path('departamento/', views.Departamentos.as_view()),
    path('ubicacion/<id>/', views.UbicacionDetalle.as_view()),
    path('ubicacion/', views.Ubicaciones.as_view()),
    path('perfil/<id>/', views.PerfilDetalle.as_view()),
    path('perfil/', views.Perfiles.as_view()),
    path('empleado/<id>/', views.EmpleadoDetalle.as_view()),
    path('empleado/', views.Empleados.as_view()),    
    path('usuario/<id>/', views.UsuarioDetalle.as_view()),
    path('usuario/', views.Usuarios.as_view()),
]