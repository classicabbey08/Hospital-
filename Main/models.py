from django.db import models

# Create your models here.

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    DEPARTMENT_CHOICES = [
        ('diagnostic', 'Diagnostic'),
        ('psychological', 'Psychological'),
    ]

    DOCTOR_CHOICES = [
        ('doctor_a', 'Doctor A'),
        ('doctor_b', 'Doctor B'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    doctor = models.CharField(max_length=50, choices=DOCTOR_CHOICES)
    appointment_date = models.DateField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.appointment_date}"
