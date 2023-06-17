from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.Main,name="Main"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('order',views.order,name="order"),
    path('buy',views.buy,name="buy")
]
