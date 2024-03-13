#3/12/2024; test file for exercise 11-1
from city_functions import city_country

def test_city_country_population():
    """test for city, country, and population if parameter used"""
    formatted_location = city_country("anaheim", "california", 344461)
    assert formatted_location == "Anaheim, California - population 344461."
def test_city_country():
    """test only for city, country parameters"""
    formatted_location = city_country("los angeles", "california")
    assert formatted_location == "Los Angeles, California."