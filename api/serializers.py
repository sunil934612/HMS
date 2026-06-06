from rest_framework import serializers
from myapp .models import Patient
from myapp .models import Appointment
from myapp.models import Doctor

class PatientsSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        
class AppointmentsSerializers(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    specialization = serializers.StringRelatedField()
    class Meta:
        model = Appointment
        fields = "__all__"        
        
class DoctorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor 
        fields = "__all__"   
        