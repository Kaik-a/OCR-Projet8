from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def aliment(request):
    return render(request, "aliment.html")


@login_required
def favorites(request):
    return render(request, "favorites.html")


def results(request):
    return render(request, "results.html")
