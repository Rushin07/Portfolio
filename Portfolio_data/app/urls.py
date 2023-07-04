from app import views
from django.urls import path, include

urlpatterns = [
    path('', views.index,name="index"),
    path('contact', views.contact,name="contact"),
    path('about', views.about, name="about"),
    path('reverse_pgm', views.reverse_pgm, name="reverse_pgm"),

]