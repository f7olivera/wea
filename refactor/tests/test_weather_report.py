import unittest
from refactor.weather import WeatherReport
from refactor.weather_condition import Temperature, Wind, RainfallRate, Pressure, Visibility
from refactor.unit import *
from colorama import Fore


class TestWeatherReport(unittest.TestCase):
    def test_temperature(self):
        temperature = Temperature(StandardUnit.TEMPERATURE, 20, 'blue')
        wind = Wind(ImperialUnit.VELOCITY,
                    velocity=15, intensity_color="yellow", direction=360)
        rain = RainfallRate(3.47)
        pressure = Pressure(1000)
        visibility = Visibility(MetricUnit.DISTANCE, 10)

        self.assertEqual(temperature.intensity_color, 'blue')
        self.assertEqual(temperature.__str__(), f'20 K')


if __name__ == '__main__':
    unittest.main()
