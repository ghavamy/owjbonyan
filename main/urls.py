from django.urls import path

from . import views 

urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("service" ,views.service, name = "service"),
    path("blog", views.blog, name = "blog"),
    path("contact", views.contact, name = "contact")
]