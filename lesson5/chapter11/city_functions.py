def cityName(city, country, population=""):
    city = city.title()
    country = country.title()
    if population != "":
        name = city + ", " + country + " - population " + population
    else:
        name = city + ", " + country
    return name