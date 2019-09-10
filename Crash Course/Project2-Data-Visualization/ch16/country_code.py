# CH16 Example
#
# country_code.py
#
# Parsing JSON files
# Obtaining two-digit country codes

# pygal.i18n was removed and is now found in pygal_maps_world
# pip3 install pygal_maps_world
from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """
    Return the Pygal 2-digit country code for a given country
    """

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # If country was not found, return nothing
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('Brazil'))
# print(get_country_code('Turkey'))
