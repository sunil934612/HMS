from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Patient
from myapp.models import Appointment
from myapp.models import Doctor
from .serializers import PatientsSerialiers
from .serializers import AppointmentsSerializers
from .serializers import DoctorsSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# add
@api_view(['GET','POST'])
def patients(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientsSerialiers(patients,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PatientsSerialiers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# update
@api_view(['GET','PUT','DELETE'])    
def patientsview(request, pk):
    try:
        patient = Patient.objects.get(pk = pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PatientsSerialiers(patient)     
        return Response(serializer.data,status=status.HTTP_200_OK) 
    elif request.method == 'PUT':
        serializer = PatientsSerialiers(patient,data = request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
    
@api_view(['GET'])
def patients(request):
    search_query = request.GET.get('search', None)
    if search_query:
        patients = Patient.objects.filter(name__icontains=search_query)
    else:
        patients = Patient.objects.all()

    serializer = PatientsSerialiers(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)  

@api_view(["GET","POST"])
def appointment(request):
    if request.method == 'GET':
       appointments = Appointment.objects.all()   
       serializer = AppointmentsSerializers(appointments,many = True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PatientsSerialiers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])        
def appointmentview(request,id):
    try:
        appointments = Appointment.objects.get(id= id)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
        
    if request.method == 'GET':
        serializer = AppointmentsSerializers(appointments)     
        return Response(serializer.data,status=status.HTTP_200_OK) 
    elif request.method == 'PUT':
        serializer = AppointmentsSerializers(appointments,data = request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
@api_view(['GET'])
def doctors_d(request):
    doctors = Doctor.objects.all()
    serializer = DoctorsSerializers(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])    
def doctors_view(request, id):
    try:
        patient = Doctor.objects.get(id = id)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DoctorsSerializers(patient)     
        return Response(serializer.data,status=status.HTTP_200_OK) 
    elif request.method == 'PUT':
        serializer = DoctorsSerializers(patient,data = request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     