
from django.urls import path, include
from . import views
app_name = 'api'
urlpatterns = [
    path('estado/<id>/', views.EstadoDetalle.as_view(), name='estado-detalle'),
    path('estado/', views.Estados.as_view(), name='estado'),
    path('empresa/<id>/', views.EmpresaDetalle.as_view(), name='empresa-detalle'),
    path('empresa/', views.Empresas.as_view(), name='empresa'),
    path('empresa-grupo/<id>/', views.EmpresaGrupoDetalle.as_view(), name='empresa-grupo-detalle'),
    path('empresa-grupo/', views.EmpresaGrupos.as_view(), name='empresa-grupo'),
    path('departamento/<id>/', views.DepartamentoDetalle.as_view(), name='departamento-detalle'),
    path('departamento/', views.Departamentos.as_view(), name='departamento'),
    path('feriado/<id>/', views.FeriadoDetalle.as_view(), name='feriado-detalle'),
    path('feriado/', views.Feriados.as_view(), name='feriado'),
    path('calendario/<id>/', views.CalendarioDetalle.as_view(), name='calendario-detalle'),
    path('calendario/', views.Calendarios.as_view(), name='calendario'),
    path('dia/<id>/', views.DiaDetalle.as_view(), name='dia-detalle'),
    path('dia/', views.Dias.as_view(), name='dia'),
    path('franja-tiempo/<id>/', views.FranjaTiempoDetalle.as_view(), name='franja-tiempo-detalle'),
    path('franja-tiempo/', views.FranjaTiempos.as_view(), name='franja-tiempo'),
    path('dia-franja-tiempo/<id>/', views.DiaFranjaTiempoDetalle.as_view(), name='dia-franja-tiempo-detalle'),
    path('dia-franja-tiempo/', views.DiaFranjaTiempos.as_view(), name='dia-franja-tiempo'),
    path('ubicacion/<id>/', views.UbicacionDetalle.as_view(),name='ubicacion-detalle'),
    path('ubicacion/', views.Ubicaciones.as_view(), name='ubicacion'),
    path('perfil/<id>/', views.PerfilDetalle.as_view(), name='perfil-detalle'),
    path('perfil/', views.Perfiles.as_view(), name='perfil'),
    path('empleado/<id>/', views.EmpleadoDetalle.as_view(), name='empleado-detalle'),
    path('empleado/', views.Empleados.as_view(), name='empleado'),    
    path('usuario/<id>/', views.UsuarioDetalle.as_view(), name='usuario-detalle'),
    path('usuario/', views.Usuarios.as_view(), name='usuario'),
    path('empleado-ubicacion/<id>/', views.EmpleadoUbicacionDetalle.as_view(), name='empleado-ubicacion-detalle'),
    path('empleado-ubicacion/', views.EmpleadoUbicaciones.as_view(), name='empleado-ubicacion'),    
    path('token/', views.GeneralTokenView.as_view(), name='token-general'),
    path('login-app/', views.LoginAppView.as_view(), name='login-app'),
]

