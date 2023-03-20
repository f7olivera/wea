import unittest
from refactor.weather_condition import *
from refactor.unit import *


class TestWeatherCondition(unittest.TestCase):
    def test_temperature(self):
        temperature = Temperature(StandardUnit.TEMPERATURE, 20, 'blue')

        self.assertEqual(temperature.intensity_color, 'blue')
        self.assertEqual(temperature.__str__(), f'20 K')

    def test_wind(self):
        wind = Wind(ImperialUnit.VELOCITY,
                    velocity=15, intensity_color="yellow", direction=360)

        self.assertEqual(wind.intensity_color, 'yellow')
        self.assertEqual(wind.__str__(), f'↓  15 mph')

    def test_rain(self):
        rain = RainfallRate(3.47)

        self.assertEqual(rain.__str__(), '3.47 mm')

    def test_pressure(self):
        pressure = Pressure(1000)

        self.assertEqual(pressure.__str__(), '1000 hPa')

    def test_visibility(self):
        visibility = Visibility(MetricUnit.DISTANCE, 10)

        self.assertEqual(visibility.__str__(), '10 km')


if __name__ == '__main__':
    unittest.main()
