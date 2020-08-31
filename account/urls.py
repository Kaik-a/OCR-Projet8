from django.urls import path

from . import views

urlpatterns = [
    path('authenticate/', views.login),
    path('login/', views.get_user_info),
    path('subscription/', views.subscribe),
    path('logout/', views.sign_out)
]
