from django.shortcuts import render


def index(request):
    return render(request, "../templates/index.html")


def about(request):
    return render(request, "../templates/about.html")


