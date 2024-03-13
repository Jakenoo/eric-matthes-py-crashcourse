#3/12/2024; exercise 11-1
def city_country(city, country, population=""):
    """returns formatted string of city, country, and population"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}."
    else:
        return f"{city.title()}, {country.title()}."