from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    city_name = serializers.CharField(max_length=100)
    lang = serializers.CharField(max_length=2)
    temp = serializers.FloatField()
    min_temp = serializers.FloatField()
    max_temp = serializers.FloatField()
    humidity = serializers.FloatField()
    wind_speed = serializers.FloatField()
    direction = serializers.CharField(max_length=100)
    pressure = serializers.FloatField()
    description = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
