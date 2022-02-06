import re
import math
import itertools
from requests import get
from pytz import timezone, utc, UnknownTimeZoneError
from datetime import datetime
from timezonefinder.command_line import tf
from wea.backend import config
from wea.frontend import translations

BASE_URL = 'https://nominatim.openstreetmap.org/'


def get_geocoding_response(location=str):
    """
    Returns a list of geocoded locations.
    """
    location = re.findall(r'\w+', location)
    location = '+'.join(location)
    lang = config.get_user_config.__wrapped__()['Preferences']['lang']
    geocoded_locations = get(f'{BASE_URL}search.php?q={location}&format=jsonv2&accept-language={lang}').json()
    if not geocoded_locations:
        print(translations.unknown_location[lang])
        exit()
    return geocoded_locations


def get_places(location):
    """
    Generates a dictionary of locations geocoded by Nominatim.
    """
    places = {}
    cities = 10
    place_response = get_geocoding_response(location)
    delete_close_together(place_response, 10)
    for place in place_response:
        # Ensures that the places are not too broad
        # More about place ranking in https://nominatim.org/release-docs/develop/customize/Ranking/
        if place['place_rank'] >= cities:
            place_name = place['display_name']
            places[place_name] = format_location(place)
    return places


def delete_close_together(places, maximum_separation):
    """
    Filters places that are too close to each other, prioritazing the one with the smaller rank.

    :param places: a list of places generated by the geocoding tool from Nominatim.
    :param maximum_separation: maximum distance (in kilometers) for two places to be considered "close".
    """

    for place1, place2 in itertools.combinations(places[:], 2):
        coord1 = [float(place1['lat']), float(place1['lon'])]
        coord2 = [float(place2['lat']), float(place2['lon'])]
        if get_distance(coord1, coord2) < maximum_separation:
            rank_i = place1['place_rank']
            rank_j = place2['place_rank']
            place_greater_rank = place1 if rank_i > rank_j else place2
            places.remove(place_greater_rank)


def format_location(location):
    location['coord'] = [float(location['lat']), float(location['lon'])]
    timezone_offset = get_offset(lat=location['coord'][0],
                                 lng=location['coord'][1])
    return {
        'name': location['display_name'].split(',')[0],
        'full_name': location['display_name'],
        'coord': location['coord'],
        'timezone_offset': timezone_offset
    }


def get_distance(coord1, coord2):
    """
    Returns the approximate distance between two geographical coordinates.
    """
    earth_radius_km = 6371
    lat1 = coord1[0] * math.pi / 180
    lon1 = coord1[1] * math.pi / 180
    lat2 = coord2[0] * math.pi / 180
    lon2 = coord2[1] * math.pi / 180

    # Haversine formula
    a = math.sin(abs(lat1 - lat2) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * \
        math.sin(abs(lon1 - lon2) / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius_km * c


def get_offset(lat, lng):
    try:
        today = datetime.now()
        tz_target = timezone(tf.certain_timezone_at(lng=lng, lat=lat))
        today_target = tz_target.localize(today)
        today_utc = utc.localize(today)
        return (today_utc - today_target).total_seconds()

    except UnknownTimeZoneError:
        print(f'Couldn\'t determine the timezone for {lat} {lng}.')