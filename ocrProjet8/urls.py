from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', include('catalog.urls')),
    path('search/', include('search.urls')),
    path('accounts/', include('accounts.urls')),
    path('notice', views.legal_notice, name='notice'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

