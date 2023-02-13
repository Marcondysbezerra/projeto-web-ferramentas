from django.urls import path

from website.meuapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ipv4/', views.ip_address_v4, name='ipv4')
]