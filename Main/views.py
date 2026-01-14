from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def appointment(request):
    return render(request, "appointment.html")


def contact(request):
    return render(request, "contact.html")


def contact_success(request):
    return render(request, "contact_success.html")


def blog(request):
    return render(request, "blog.html")


def service(request):
    return render(request, "support.html")


def gallery(request):
    return render(request, "gallery.html")


def team(request):
    return render(request, "team.html")
