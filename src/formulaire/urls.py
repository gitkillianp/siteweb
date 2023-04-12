from django.urls import path
from formulaire.views import formulaire

app_name = "formulaire"

urlpatterns = [
    path('', formulaire, name="formulaire"),
]
