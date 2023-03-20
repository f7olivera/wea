from enum import Enum


class UnitSystem(Enum):
    STANDARD = 0
    IMPERIAL = 1
    METRIC = 2


class StandardUnit(Enum):
    PRESSURE = 'hPa'
    RAINFALL_RATE = 'mm'
    VELOCITY = 'm/s'
    TEMPERATURE = 'K'
    DISTANCE = 'km'


class ImperialUnit(Enum):
    PRESSURE = 'hPa'
    RAINFALL_RATE = 'mm'
    VELOCITY = 'mph'
    TEMPERATURE = '°F'
    DISTANCE = 'mi.'


class MetricUnit(Enum):
    PRESSURE = 'hPa'
    RAINFALL_RATE = 'mm'
    VELOCITY = 'm/s'
    TEMPERATURE = '°C'
    DISTANCE = 'km'
