from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    hallticket = models.CharField(max_length=100)
    branch  = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    
    
class Specialization(models.Model):
    sname = models.CharField(max_length=100)

    def __str__(self):
        return self.sname


class Doctor(models.Model):
    
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    mobilenumber = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='doctor_pics/', blank=True, null=True)  

    def __str__(self):
        return f"{self.name} ({self.specialization.sname})"


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending...', 'Pending...'),
        ('Approved', 'Approved'),
        ('Canceled', 'Canceled'),
    )
    name = models.CharField(max_length=100)  # Full Name of patient
    mobilenumber = models.CharField(max_length=10)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # <-- select field
    date = models.DateField()
    time = models.TimeField()
    msg = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  


    def __str__(self):
        return f"{self.name} - {self.doctor.name} on {self.date}"
    
    
class Patient(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    name = models.CharField(max_length=100)   # Full Name
    mobilenumber = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    age = models.PositiveIntegerField()
    medhistory = models.TextField(blank=True, null=True)  # Medical history if any
    created_at = models.DateTimeField(auto_now_add=True) 
   

    def __str__(self):
        return f"{self.name} ({self.age} yrs)"   
    
class About(models.Model):
    About_us = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    message = models.TextField()    
    
    