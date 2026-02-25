"""Catalogos para peticiones de la API de INEGI."""

from enum import IntEnum


class StatesCodes(IntEnum):
    """Códigos de estados de México."""
    MX = 0  # Todo el país
    AGUASCALIENTES = 1
    BAJA_CALIFORNIA = 2
    BAJA_CALIFORNIA_SUR = 3
    CAMPECHE = 4
    CHIAPAS = 5
    CHIHUAHUA = 6
    CDMX = 7
    COAHUILA = 8
    COLIMA = 9
    DURANGO = 10
    GUANAJUATO = 11
    GUERRERO = 12
    HIDALGO = 13
    JALISCO = 14
    MICHOACAN = 15
    MORELOS = 16
    MEXICO = 17
    NAYARIT = 18
    NUEVO_LEON = 19
    OAXACA = 20
    PUEBLA = 21
    QUERETARO = 22
    QUINTANA_ROO = 23
    SAN_LUIS_POTOSI = 24
    SINALOA = 25
    SONORA = 26
    TABASCO = 27
    TAMAULIPAS = 28
    TLAXCALA = 29
    VERACRUZ = 30
    YUCATAN = 31
    ZACATECAS = 32

if __name__ == "__main__":
    from pprint import pprint
    pprint(StatesCodes.__members__)
