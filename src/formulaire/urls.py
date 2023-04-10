from django.urls import path
from .views import formulaire

app_name = "formulaire"

urlpatterns = [
    path('', formulaire, name="formulaire"),
]
