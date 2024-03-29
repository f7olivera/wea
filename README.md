wea is an ASCII decorated command-line program to get a weather report in your terminal, for any location and in multiple languages.

![](https://github.com/f7olivera/wea/blob/dc89a02c970af8fb3477709f068d271d19742dad/example.gif)

## Features
- Current weather report.
- Forecast for the next 5 days.
- Several weather conditions:
    -  Temperature and apparent temperature.
    -  Wind direction and speed.
    -  Atmospheric pressure.
    -  Rainfall rate and probability of precipitation.
    -  Visibility distance.
- Metric and imperial unit system.
- Multilingual support.

## Setup
You will need
- [Python >= 3.6](https://www.python.org/)
- [pip](https://pypi.org)
- a free API key for OpenWeather. You can find yours [here](https://home.openweathermap.org/api_keys), after signing in.

## Instalation
You can install wea using [pip](https://pypi.org):

    pip install wea-clt

## Usage
You can see all available commands typing
    
    wea -h

which displays the following help message:
```
usage: wea [-h] [-c | -f | -l  [...] | -u [default | metric | imperial] | --lang  | -k  | --config]

options:
  -h, --help            show this help message and exit
  -c, --current         Shows current weather for the set location.
  -f, --forecast        Shows weather forecast for the set location.
  -l  [ ...], --location  [ ...]
                        Sets a location.
  -u [default | metric | imperial], --units [default | metric | imperial]
                        Changes unit system
  --lang                Sets new language.
  -k , --key            Sets the OpenWeather API key.
  --config              Shows current user configuration path and content.
```

If no arguments were provided, wea shows current and weather forecast for the location set in the user's configuration file.

You can also see a weather report for a location without changing the configuration file. Try:

	wea London -c

## License
wea is released under the [MIT License](https://github.com/f7olivera/wea/blob/master/LICENSE).

This project uses source code from the files
- `translations.py` from https://github.com/chubin/wttr.in, licensed under the [Apache License 2.0](https://github.com/chubin/wttr.in/blob/master/LICENSE).
- `ascii-art-table.go` from https://github.com/schachmat/wego, Copyright (c) 2014-2017,  <teichm@in.tum.de>, licensed under the [ISC License](https://github.com/schachmat/wego/blob/master/LICENSE).
