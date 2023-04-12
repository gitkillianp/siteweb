from django import forms
from .models import FormulaireModel

PROBLEMES = (
    ("WiFi", "Problème avec mon réseau Wifi"),
    ("Virus", "Suspicion de virus sur mon réseau"),
    ("Nettoyage", "Nettoyage de mon ordinateur"),
    ("Développement web", "Initiation au développement web"),
    ("Cours", "Cours informatique tout niveau"),
    ("Dépannage", "Dépannage informatique, problème matériel"),
    ("Récupération données", "Récupération de données"),
    ("Autre", "(Autre)"),
)

LOCALITE = (
    ("Longjumeau", "Longjumeau"),
    ("Ballainvilliers", "Ballainvilliers"),
    ("Brétigny sur Orge", "Brétigny-sur-Orge"),
    ("Longpont sur Orge", "Longpont-sur-Orge"),
    ("Villiers sur Orge", "Villiers-sur-Orge"),
    ("Savigny sur Orge", "Savigny-sur-Orge"),
    ("Epinay sur Orge", "Épinay-sur-Orge"),
    ("Ville du Bois", "Ville-du-Bois"),
    ("Nozay", "Nozay"),
    ("Linas", "Linas"),
    ("Montlhéry", "Montlhéry"),
    ("Autre", "(Autre)"),
)


class Formulaire(forms.ModelForm):
    class Meta:
        model = FormulaireModel
        fields = [
            "Email",
            "Type",
            "Localité",
            "Description",
        ]



