from django.urls import path

from . import views

urlpatterns = [
    path('aliment/', views.aliment),
    path('favorites/', views.favorites),
    path('results/', views.results)
]
