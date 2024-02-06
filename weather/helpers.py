from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.core.cache import cache
import os
from dotenv import load_dotenv
import requests
from .serializers import WeatherSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import deg_to_direction
from drf_spectacular.utils import extend_schema
from django.http import JsonResponse

load_dotenv()

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


api_key = os.getenv("API_KEY")
unit = "metric"


# Gets the coordinates of the city
def fetch_coord(city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"

    cached_data = cache.get(url)
    if cached_data is not None:
        return cached_data

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if not data:
        return None
    else:
        cache.set(url, data, timeout=CACHE_TTL)
        return data


# Gets the weather details of the city
def fetch_weather(lat, lon, lang):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={unit}&lang={lang}&appid={api_key}"

    cached_data = cache.get(url)
    if cached_data is not None:
        return cached_data

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if not data:
        return None
    else:
        cache.set(url, data, timeout=CACHE_TTL)
        return data


@extend_schema(
    request=WeatherSerializer,
    responses=None,
    description="Fetch Weather Details from OpenWeatherMap by entering city name and language code.",
)
@extend_schema(methods=["POST"], exclude=True)
@api_view(["GET", "POST"])
def fetch_city_weather(request, city_name, lang="en"):

    if len(lang) != 2:
        message = "Please enter two letter language code."
        status_code = 406
        return JsonResponse({"message": message}, status=status_code)

    location_data = fetch_coord(city_name)

    if location_data is None:
        message = "City not found, please enter a valid city!"
        status_code = 404
        return JsonResponse({"message": message}, status=status_code)

    lat = location_data[0]["lat"]
    lon = location_data[0]["lon"]

    weather_data = fetch_weather(lat, lon, lang)

    data_dict = {
        "temp": weather_data["main"]["temp"],
        "min_temp": weather_data["main"]["temp_min"],
        "max_temp": weather_data["main"]["temp_max"],
        "humidity": weather_data["main"]["humidity"],
        "pressure": weather_data["main"]["pressure"] / 1000,
        "wind_speed": weather_data["wind"]["speed"],
        "direction": deg_to_direction(weather_data["wind"]["deg"]),
        "description": weather_data["weather"][0]["description"],
        "city_name": weather_data["name"],
        "lang": lang,
        "country": weather_data["sys"]["country"],
    }

    serializer = WeatherSerializer(data_dict)

    return JsonResponse(serializer.data)
