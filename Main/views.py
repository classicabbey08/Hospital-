from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import Contact
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Appointment


def home(request):
    if request.method == "POST":
        appointment = Appointment.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            department=request.POST.get("department"),
            doctor=request.POST.get("doctor"),
            appointment_date=request.POST.get("appointment_date"),
            message=request.POST.get("message"),
        )

        send_mail(
            subject="New Appointment Request",
            message=f"""
New Appointment Request

Name: {appointment.name}
Email: {appointment.email}
Phone: {appointment.phone}
Department: {appointment.department}
Doctor: {appointment.doctor}
Date: {appointment.appointment_date}

Message:
{appointment.message}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        return redirect("appointment_success")
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

def appointment_success(request):
    return render(request, "appointment_success.html")





from django.shortcuts import render

def about(request):
    faq_questions = [
        "Why choose Medical Health?",
        "Visiting hours?",
        "Visitors allowed?"
    ]
    return render(request, "about.html", {"faq_questions": faq_questions})
