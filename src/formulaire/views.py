from django.shortcuts import render
from formulaire.forms import Formulaire
from django.core.mail import send_mail
from django.conf import settings

def formulaire(request):
    if request.method == "POST":
        form = Formulaire(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            # Envoi de l'e-mail
            subject = "Nouvelle soumission de formulaire"
            message = "Voici les données soumises :\n" + str(form.cleaned_data)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['contact@urgencepc91.fr', 'killian.pasche@gmail.com']
            send_mail(subject, message, email_from, recipient_list)

            form.save()
            return render(request, "../templates/réponse.html")
    else:
        form = Formulaire()

    return render(request, "../templates/formulaire.html", {"form": form})
