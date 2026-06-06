from django.urls import path,include
from .import views

urlpatterns = [
    path('patients/',views.patients),
    path('patients/<int:pk>/',views.patientsview),
    path('appointments/',views.appointment),
    path('appointments/<int:id>/',views.appointmentview,name='appointmentss'),
    path('doctors/',views.doctors_d),
    path('doctors/<int:id>/',views.doctors_view)

]