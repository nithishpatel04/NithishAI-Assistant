import requests


def get_weather(city: str) -> dict:
    """
    Get current weather information for a city.

    Use this tool when the user asks about current weather,
    temperature, rain, or weather-related recommendations.
    """

    print(f"TOOL CALLED: get_weather({city})")

    # Find coordinates for the city
    geo_response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json",
        },
        timeout=10,
    )

    geo_response.raise_for_status()

    geo_data = geo_response.json()

    if not geo_data.get("results"):
        return {
            "error": f"Could not find location: {city}"
        }

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    # Retrieve current weather
    weather_response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "apparent_temperature,"
                "precipitation,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto",
        },
        timeout=10,
    )

    weather_response.raise_for_status()

    weather = weather_response.json()["current"]

    return {
        "city": location["name"],
        "country": location.get("country"),
        "temperature_c": weather["temperature_2m"],
        "feels_like_c": weather["apparent_temperature"],
        "precipitation_mm": weather["precipitation"],
        "wind_speed_kmh": weather["wind_speed_10m"],
        "weather_code": weather["weather_code"],
    }