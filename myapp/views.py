from django.shortcuts import render,redirect
from .models import Student
from .models import Appointment, Specialization
from .models import Doctor
from.models import About
from .models import Contact
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

from.models import Patient
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import PatientsSerialiers
from rest_framework import status
from django.shortcuts import get_object_or_404

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Logs the user in
            return redirect('doctor')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('signin')
    
    return render(request, 'login.html')


   
        

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()  # create_user already saves, but it's fine to call

        messages.success(request, "Account created successfully. Please login.")
        return redirect('signin')  # redirect to login page

    return render(request, 'signup.html')



def patient(request):
        if request.method == "POST":
         name = request.POST.get("name")
         mobilenumber = request.POST.get("mobilenumber")
         email = request.POST.get("email")
         gender = request.POST.get("gender")
         address = request.POST.get("address")
         age = request.POST.get("age")
         medhistory = request.POST.get("medhistory")
         Patient.objects.create(
            name = name,
            mobilenumber=mobilenumber,
            email=email,
            gender=gender,
            address=address,
            age=age,
            medhistory=medhistory,
        )
         messages.success(request, "Patient added successfully ")

         
        return render(request,'add_patient.html',{"patient":Patient })
def manage (request):
    patients = Patient.objects.all()
    return render(request,'manage_patient.html',{"patient_manage":patients}) 

def manage(request):
    search_query = request.GET.get("search", "") 

    if search_query:
        patients = Patient.objects.filter(
            Q(name__icontains=search_query) |
            Q(mobilenumber__icontains=search_query)
        )
    else:
        patients = Patient.objects.all()

    total_patient = patients.count()  

    return render(request, 'manage_patient.html', {
        "patient_manage": patients,
        "search_query": search_query,
        "total_patient": total_patient
    })
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, f"Patient {patient.name} deleted successfully.")
    return redirect('manage')


def patient_details(request, id):
    # Get the particular patient from DB
    patient = get_object_or_404(Patient, id=id)
    
    # Get all appointments for this patient
    appointments = Appointment.objects.filter(mobilenumber=patient.mobilenumber)
    
    return render(request, 'patient_appointment_details.html', {
        "patient": patient,
        "app_det": appointments
    })



def doc(request):
    return render(request,'index.html')


def app(request):
    return render (request,'appointment.html')

def base(request):
    return render(request,'userbase.html')

def about(request):
    aboutus = About.objects.all()
    return render(request,'aboutus.html',{"about":aboutus})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        message = request.POST.get("message")
        Contact.objects.create(
            name = name,
            email = email,
            contact = contact,
            message = message
        )
        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')

    return render(request,'contactus.html')
def doctor(request):
    doctors = Doctor.objects.all()
    return render(request,'doctor.html',{"doctors":doctors})

def history(request):
    search_query = request.GET.get("search", "")

    appointments = Appointment.objects.all() 
    
    
    
    if search_query:
        appointments = appointments.filter(
            Q(name__icontains=search_query) |
            Q(mobilenumber__icontains=search_query) 
           
        )
    return render(request,'appointment-history.html',{'appointments':appointments,"search_query": search_query})

def appointments(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobilenumber = request.POST.get("mobilenumber")
        specialization_id = request.POST.get("specialization")
        doctor_id = request.POST.get("doctor")
        date = request.POST.get("date")
        time = request.POST.get("time")
        msg = request.POST.get("msg")

        specialization = get_object_or_404(Specialization, id=specialization_id)
        doctor = get_object_or_404(Doctor, id=doctor_id)

        Appointment.objects.create(
            name=name,
            mobilenumber=mobilenumber,
            specialization=specialization,
            doctor=doctor,
            date=date,
            time=time,
            msg=msg
        )

    specializations = Specialization.objects.all()
    doctors = Doctor.objects.all()
    messages.success(request,"Appointment Sucess")
    
    return render(request,'appointments.html',
        {"specializations": specializations, "doctors": doctors}
    )

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = 'Canceled'
    appointment.save()
    return redirect('details')  
def delete(request, appointment_id):
    app = get_object_or_404(Appointment,id= appointment_id)
    app.status='Delete'
    app.delete()
    return redirect('details')

def admins(request):
    docs = Doctor.objects.all()
    docs_count = docs.count()
    total = Patient.objects.all()
    patient_total = total.count()
    return render(request,'admin/admin.html',{'doctors': docs, 'doctors_count': docs_count,"totals":patient_total,"pat":total})


def doc_list(request):
    doc_lists = Doctor.objects.all()
    return render(request,'doctor/doctor_list.html',{"details":doc_lists})

def doctor_details(request, id):
    doctor_details = get_object_or_404(Doctor, id=id)   # fetch only that doctor
    return render(request, "doctor/doctor_details.html", {"doctor_details": doctor_details})


 



def register_patient(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register_patient")

        user = User.objects.create_user(username=username, email=email, password=password)

        # Add user to Patient group
        patient_group, created = Group.objects.get_or_create(name="Patient")
        user.groups.add(patient_group)

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "register_patient.html")





def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)   
            return redirect("admin_home")  
        else:
            return render(request, "ulogin.html", {"error": "Invalid username or password"})

    return render(request, "ulogin.html")
  