from django.shortcuts import render
from formulaire.forms import Formulaire


def formulaire(request):
    if request.method == "POST":
        form = Formulaire(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return render(request, "../templates/réponse.html")

    else:
        form = Formulaire()

    return render(request, "../templates/formulaire.html", {"form": form})
