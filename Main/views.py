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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                subject=f"New Contact Form: {contact.subject}",
                message=f"""
Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone}

Message:
{contact.message}
                """.strip(),
                from_email="PrimeMed Contact Form <classicabbey08@gmail.com>",
                recipient_list=["muleroabiodun705@gmail.com"],
                fail_silently=False,
            )

            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


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
