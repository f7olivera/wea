from weather_condition import *
from unit import *


def main():
    print("Hello World!")
    wind = Wind(ImperialUnit.VELOCITY, 15, "yellow", "north")
    rain = RainfallRate(15)
    pressure = Pressure(20)
    visibility = Visibility(MetricUnit.DISTANCE, 10)


if __name__ == "__main__":
    main()
