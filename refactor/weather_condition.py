from abc import ABC, abstractmethod
from enum import Enum
from refactor.unit import StandardUnit, ImperialUnit


class WeatherCondition(ABC):
    """
    Class that contains a weather condition and its unit.

    Attributes:
        unit (Enum): The unit of the weather condition.
        value (float): The value of the weather condition.
    """
    @abstractmethod
    def __init__(self, unit: Enum, value):
        self.unit = unit
        self.value = value

    @abstractmethod
    def convert(self, unit):
        """
        Converts the weather condition to a different unit.

        param unit: The unit to convert to.
        """
        pass

    def __str__(self):
        return f'{self.value} {str(self.unit.value)}'


class Temperature(WeatherCondition):
    def __init__(self, unit, value, apparent_value):
        super().__init__(unit, value)
        self.apparent_value = apparent_value

    def convert(unit):
        pass

    def get_intensitiy_color(self):
        if self.unit == StandardUnit.TEMPERATURE:
            metric_value = self.value - 273.15
        elif self.unit == ImperialUnit.TEMPERATURE:
            metric_value = int((self.value - 32) * 5 / 9)

        if metric_value < -15:
            return Fore.LIGHTBLUE_EX
        if metric_value < 0:
            return Fore.LIGHTMAGENTA_EX
        if metric_value < 6:
            return Fore.LIGHTWHITE_EX
        if metric_value < 16:
            return Style.RESET_ALL
        if metric_value < 26:
            return BRIGHTYELLOW
        if metric_value < 33:
            return Fore.LIGHTGREEN_EX
        else:
            return Fore.RED

    def __str__(self):
        return f'{self.value}({self.apparent_value}) {str(self.unit.value)}'


class Wind(WeatherCondition):
    def __init__(self, unit, velocity, direction):
        super().__init__(unit, velocity)
        self.direction = direction

    def convert(self, unit):
        pass

    def get_wind_direction(self) -> str:
        direction = self.direction
        if 337.5 <= direction or direction < 22.5:
            return '↓'
        elif 22.5 <= direction < 67.5:
            return '↙'
        elif 67.5 <= direction < 112.5:
            return '←'
        elif 112.5 <= direction < 157.5:
            return '↖'
        elif 157.5 <= direction < 202.5:
            return '↑'
        elif 202.5 <= direction < 247.5:
            return '↗'
        elif 247.5 <= direction < 292.5:
            return '→'
        elif 292.5 <= direction < 337.5:
            return '↘'

    def get_intensitiy_color(self):
        if self.unit == ImperialUnit.VELOCITY:
            metric_velocity = self.value * 1.609
        metric_velocity = int(self.value)

        if 5 <= metric_velocity < 16:
            return BRIGHTYELLOW
        if 16 <= metric_velocity < 25:
            return Fore.LIGHTGREEN_EX
        if 25 <= metric_velocity < 30:
            return Fore.GREEN
        if 30 <= metric_velocity:
            return Fore.RED
        else:
            return ''

    def __str__(self):
        return f"{self.get_wind_direction()}  {super().__str__()}"


class RainfallRate(WeatherCondition):
    def __init__(self, value):
        super().__init__(StandardUnit.RAINFALL_RATE, value)

    def convert(self, unit):
        pass


class Pressure(WeatherCondition):
    def __init__(self, value):
        super().__init__(StandardUnit.PRESSURE, value)

    def convert(self, unit):
        pass


class Visibility(WeatherCondition):
    def __init__(self, unit, value):
        super().__init__(unit, value)

    def convert(self, unit):
        pass
