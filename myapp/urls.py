from django.urls import path,include
from .import views
from django.shortcuts import redirect

urlpatterns = [
    path('',lambda request:redirect('home')),
    path('home/',views.doc,name='home'),
    path('appointment/',views.app,name='appointment'),
    path('base/',views.base,name='base'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('doctors/',views.doctor,name='doctor'),
    path('doctor/login/',views.login,name='signin'),
    path('doctor/signup/',views.signup,name='signup'),
    path('add/patient/details/',views.patient,name='patient'),
    path('appointment/details/',views.history,name='details'),
    path('patient_details/<int:id>/',views.patient_details,name='patient_details'),
    path('add/appointments/',views.appointments,name='appointments'),
    path('manage/patients/details/',views.manage,name='manage'),
    path('delete_patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('delete-appointment/<int:appointment_id>/',views.delete,name='delete_appointment'),
    path('dashboard/',views.admins,name='admin_home'),
    path('doctor/list/',views.doc_list,name='doc_list'),
    path('doctor/details/<int:id>/',views.doctor_details,name='doctor_details'),
    
     path("register/admin-/", views.register_patient, name="register_patient"),
    path("admin-/home/login/", views.user_login, name="login"),
    # path("logout/", views.user_logout, name="logout"),

            # path('patients/list/', views.patients_list, name='patients_api'),

]