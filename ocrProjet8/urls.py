from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home),
    path('catalog/', include('catalog.urls')),
    path('search/', include('search.urls')),
    path('account/', include('account.urls')),
    path('notice', views.legal_notice),
    path('admin/', admin.site.urls),
]
