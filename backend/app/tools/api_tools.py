import requests


def get_country_information(country: str) -> dict:
    """
    Get current factual information about a country,
    such as capital, population, region and currencies.
    """

    print(f"TOOL CALLED: get_country_information({country})")

    url = (
        "https://restcountries.com/v3.1/name/"
        f"{country}"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()[0]

    return {
        "name": data.get("name", {}).get("common"),
        "capital": data.get("capital", []),
        "population": data.get("population"),
        "region": data.get("region"),
        "subregion": data.get("subregion"),
        "currencies": data.get("currencies", {}),
    }