from django.db import models

PROBLEMES = (
    ("WiFi", "Problème avec mon réseau (WiFi / Ethernet / autre)"),
    ("Virus", "Suspicion de virus sur mon réseau"),
    ("Nettoyage", "Nettoyage de mon ordinateur"),
    ("Leçon", "Besoin d'un cours d'informatique"),
    ("Cours logiciel", "Besoin d'un cours sur un logiciel"),
    ("Dépannage", "Dépannage informatique matériel"),
    ("Récupération données", "Récupération de données sur ordinateur ne fonctionnant plus"),
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
)


class FormulaireModel(models.Model):
    Email = models.EmailField()
    Type = models.CharField(max_length=50, choices=PROBLEMES)
    Localite = models.CharField(null=True, max_length=50, choices=LOCALITE)
    Description = models.TextField(max_length=300)

    class Meta:
        verbose_name = "Formulaire"