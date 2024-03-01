import os
import googlemaps
from langchain.tools import tool
from global_land_mask import globe


API_KEY = os.getenv("GOOGLE_API_KEY")


@tool
def reverse_geocode_agent(lat: float, lng: float) -> str:
    """ Reverse geocode a given lat/lng pair. """
    if is_on_land(lat, lng):
        site_name = get_site_name(lat, lng)
        country_name = get_country_name(lat, lng)
        return site_name, country_name, True
    else:
        return "Location off land", "No country associated", False


def is_on_land(lat, lng):
    """ Check if a given lat/lng pair is on land. """
    if globe.is_land(lat, lng):
        return True
    else:
        return False


def get_country_name(lat, lng):
    """ Get the country name of a given lat/lng pair. """
    gmaps = googlemaps.Client(key=API_KEY)
    try:
        geocode_result = gmaps.reverse_geocode((lat, lng))
        country_name = geocode_result[0]['address_components'][3]['long_name']

    except Exception as e:
        country_name = "No country"
        print(e)
    return country_name


def get_site_name(lat, lng):
    """ Get the formatted address of a given lat/lng pair. """
    gmaps = googlemaps.Client(key=API_KEY)
    try:
        geocode_result = gmaps.reverse_geocode((lat, lng))
        # formatted_address = geocode_result[1]['formatted_address']
        site_name = geocode_result[0]['address_components'][1]['long_name']
        return site_name
    except Exception as e:
        site_name = "No location"
        print(e)
        return site_name
