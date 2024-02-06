from django.shortcuts import render
from .forms import CityForm
from django.contrib import messages
from .helpers import fetch_city_weather
from asgiref.sync import sync_to_async
import json


async def home(request):
    form = CityForm()

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data["city"]
            lang = form.cleaned_data["lang"]

            weather_data = await sync_to_async(fetch_city_weather)(
                request, city_name, lang
            )

            data_dict = json.loads(weather_data.content)

            if weather_data.status_code != 200:
                data_dict = None
                messages.error(request, "City not found, please enter a valid city!")

            return render(request, "home.html", {"data": data_dict, "form": form})
        else:
            messages.error(request, "Please fill all the fields!")

    return render(request, "home.html", {"form": form})
