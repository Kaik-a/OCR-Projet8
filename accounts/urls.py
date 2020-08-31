from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('authenticate/', views.login, name='authenticate'),
    path('login/', views.get_user_info, name='login'),
    path('subscription/', views.subscribe, name='subscription'),
    path('logout/', views.sign_out, name='logout'),
    path('user_account', views.user_account, name='user_account'),
]
