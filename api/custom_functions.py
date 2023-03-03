from geopy import distance
from decimal import Decimal
from shapely import geometry

def valida_rango(tipo_dato, coordenadas_ubicacion, distancia_max, lat, lon):
    _en_rango = False
    _distancia_actual = 0
    if not coordenadas_ubicacion or not lat or not lon or not tipo_dato:
        return (_en_rango,_distancia_actual)
    if tipo_dato=="point":
        coordenada_actual = (Decimal(lat), Decimal(lon))
        coordenadas_ubicacion = (Decimal(coordenadas_ubicacion[0]["lat"]), Decimal(coordenadas_ubicacion[0]["lon"]))        
        _distancia_actual =  distance.geodesic(coordenadas_ubicacion, coordenada_actual).meters
        return _distancia_actual <= distancia_max, _distancia_actual
    if tipo_dato=="polygon":
        punto_actual = geometry.Point(Decimal(lat), Decimal(lon))
        coordenadas_ubicacion = [tuple(d.values())  for d in coordenadas_ubicacion]
        poligono_ubicacion = geometry.Polygon(tuple(coordenadas_ubicacion))
        return poligono_ubicacion.contains(punto_actual), 0
    return _en_rango, _distancia_actual