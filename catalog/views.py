from django.shortcuts import render


def aliment(request):
    return render(request, "aliment.html")


def favorites(request):
    return render(request, "favorites.html")


def results(request):
    return render(request, "results.html")
