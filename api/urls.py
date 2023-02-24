
from django.urls import path, include
from . import views
app_name = 'api'
urlpatterns = [
    path('estado/<id>/', views.EstadoDetalle.as_view(), name='estado-detalle'),
    path('estado/', views.Estados.as_view(), name='estado'),
    path('empresa/<id>/', views.EmpresaDetalle.as_view(), name='empresa-detalle'),
    path('empresa/', views.Empresas.as_view(), name='empresa'),
    path('departamento/<id>/', views.DepartamentoDetalle.as_view(), name='departamento-detalle'),
    path('departamento/', views.Departamentos.as_view(), name='departamento'),
    path('ubicacion/<id>/', views.UbicacionDetalle.as_view(),name='ubicacion-detalle'),
    path('ubicacion/', views.Ubicaciones.as_view(), name='ubicacion'),
    path('perfil/<id>/', views.PerfilDetalle.as_view(), name='perfil-detalle'),
    path('perfil/', views.Perfiles.as_view(), name='perfil'),
    path('empleado/<id>/', views.EmpleadoDetalle.as_view(), name='empleado-detalle'),
    path('empleado/', views.Empleados.as_view(), name='empleado'),    
    path('usuario/<id>/', views.UsuarioDetalle.as_view(), name='usuario-detalle'),
    path('usuario/', views.Usuarios.as_view(), name='usuario'),
    path('tipo-evento/<id>/', views.TipoEventoDetalle.as_view(), name='tipo-evento-detalle'),
    path('tipo-evento/', views.TipoEventos.as_view(), name='tipo-evento'),
]

