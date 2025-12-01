"""
Módulo de utilidades para el proyecto Campus
"""

from .helpers import (
    obtener_estadisticas_generales,
    formatear_fecha,
    validar_correo,
    calcular_promedio,
    obtener_dia_semana_numero,
    obtener_nombre_dia,
    verificar_tabla_existe
)

__all__ = [
    'obtener_estadisticas_generales',
    'formatear_fecha',
    'validar_correo',
    'calcular_promedio',
    'obtener_dia_semana_numero',
    'obtener_nombre_dia',
    'verificar_tabla_existe'
]
