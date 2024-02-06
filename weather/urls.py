from django.urls import path, include
from . import views
from . import helpers

app_name = "weather"

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "api/weather/<str:city_name>/<str:lang>",
        helpers.fetch_city_weather,
        name="get_weather",
    ),
]
