from django.contrib import admin
from .models import Student
from .models import Specialization
from .models import Doctor
from .models import Appointment
from .models import Patient
from .models import About
from .models import Contact



admin.site.register(Student)
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(About)
admin.site.register(Contact)



@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sname')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'mobilenumber')
    search_fields = ('name', 'mobilenumber')
