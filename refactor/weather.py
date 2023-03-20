from weather_condition import WeatherCondition


class WeatherReport:
    pass


class WeatherDayReport:
    morning: WeatherReport
    noon: WeatherReport
    afternoon: WeatherReport
    night: WeatherReport

    def __str__(self) -> str:
        return "[WeatherReport]"


class Weather:
    current: WeatherReport
    forecast: list[WeatherReport]
    pass
