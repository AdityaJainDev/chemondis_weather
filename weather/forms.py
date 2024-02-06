from django.forms import forms, CharField, TextInput, ChoiceField

LANGUAGES = [
    ("en", "English"),
    ("de", "German"),
    ("fr", "French"),
]


class CityForm(forms.Form):
    city = CharField(
        max_length=25,
        required=True,
        widget=TextInput(attrs={"class": "input", "placeholder": "City Name"}),
    )
    lang = ChoiceField(choices=LANGUAGES, required=True)
