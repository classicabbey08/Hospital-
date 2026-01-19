from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("appointment/", views.appointment, name="appointment"),
    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),
    path("blog/", views.blog, name="blog"),
    path("service/", views.service, name="service"),
    path("gallery/", views.gallery, name="gallery"),
    path("team/", views.team, name="team"),
        path("appointment/", views.appointment, name="appointment"),
    path("appointment/success/", views.appointment_success, name="appointment_success"),
]
