import pycountry

from myapp.models import Currency


def populate_country_list():
    """Some currency is used by multiple country codes, this will populate the appropriate countries
    for these scenarios so that missing countries are not populated incorrectly.

    Returns:
        A list of country codes.
    """
    results = []

    countries = (Currency.objects.filter(type="Coin").distinct()
                         .values_list("country", flat=True))

    countries_list = list(countries)

    for country in countries_list:
        # Eastern Carribean Islands
        if country == "CE":
            results.extend(["AI", "AG", "DM", "GD", "MS", "KN", "LC", "VC"])
        # West African CFA
        elif country == "WA":
            results.extend(["BF", "BJ", "CI", "GW", "ML", "NE", "SN", "TG"])
        # Central African CFA
        elif country == "AA":
            results.extend(["CF", "CG", "CM", "GA", "GQ", "TD"])
        # United State of America
        elif country == "US":
            results.extend(["AS", "BQ", "FM", "GU", "MH", "MP", "PR", "TC", "UM", "US", "VG", "VI"])
        # Finland
        elif country == "FI":
            results.extend(["AX", "FI"])
        # France
        elif country == "FR":
            results.extend(["BL", "FR", "MC", "MF", "MQ", "PM", "RE", "TF", "YT"])
        # Norway
        elif country == "NO":
            results.extend(["BV", "NO", "SJ"])
        # Australia
        elif country == "AU":
            results.extend(["AU", "CC", "CX", "HM", "NF", "NR", "TV"])
        # Denmark
        elif country == "DK":
            results.extend(["DK", "FO", "GL"])
        # United Kingdom
        elif country == "GB":
            results.extend(["GB", "GS", "IO"])
        # New Zealand
        elif country == "NZ":
            results.extend(["NU", "NZ", "PN", "TK"])
        # Israel
        elif country == "IL":
            results.extend(["IL", "PS"])
        else:
            results.append(country)

    return results
