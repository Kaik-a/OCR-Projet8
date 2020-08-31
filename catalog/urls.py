from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('aliment/', views.aliment, name='aliment'),
    path('favorites/', views.favorites, name='favorites'),
    path('results/', views.results, name='results')
]
