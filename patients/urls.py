from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('patients/',views.patient_list,name='patient_list'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('edit/<int:id>/',views.edit_patient,name='edit_patient'),
    path('delete/<int:id>/',views.delete_patient,name='delete_patient'),
    #doctors
    path('doctors/',views.doctor_list,name='doctor_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('edit_doctor/<int:id>/', views.edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    # Appointment
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('edit_appointment/<int:id>/', views.edit_appointment, name='edit_appointment'),
    path('delete_appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    # Billing
    path('billing/', views.billing_list, name='billing_list'),
    path('add_billing/', views.add_billing, name='add_billing'),
    path('edit_billing/<int:id>/', views.edit_billing, name='edit_billing'),
    path('delete_billing/<int:id>/', views.delete_billing, name='delete_billing'),

    path('medicine/', views.medicine_list, name='medicine_list'),
    path('add_medicine/', views.add_medicine, name='add_medicine'),
    path('edit_medicine/<int:id>/', views.edit_medicine, name='edit_medicine'),
    path('delete_medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),
    # Laboratory
    path('laboratory/', views.laboratory_list, name='laboratory_list'),
    path('add_laboratory/', views.add_laboratory, name='add_laboratory'),
    path('edit_laboratory/<int:id>/', views.edit_laboratory, name='edit_laboratory'),
    path('delete_laboratory/<int:id>/', views.delete_laboratory, name='delete_laboratory'),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path('patient/pdf/',views.patient_pdf,name='patient_pdf'),
    path('doctor/pdf/',views.doctor_pdf,name='doctor_pdf'),
    path('appointment/pdf/',views.appointment_pdf,name='appointment_pdf'),
    path('billing/pdf/',views.billing_pdf,name='billing_pdf'),
    path('medicine/pdf/',views.medicine_pdf,name='medicine_pdf'),
    path('laboratoryS/pdf/',views.laboratory_pdf,name='laboratory_pdf'),

    path('patient/excel/',views.patient_excel,name='patient_excel'),
    path('doctor/excel/',views.doctor_excel,name='doctor_excel'),
    path('appointment/excel/',views.appointment_excel,name='appointment_excel'),
    path('billing/excel/',views.billing_excel,name='billing_excel'),
    path('medicine/excel/',views.medicine_excel,name='medicine_excel'),
    path('laboratory/excel/',views.laboratory_excel,name='laboratory_excel'),

    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('activity-log/', views.activity_log, name='activity_log'),
    path('settings/', views.settings,name='settings'),
    path('about/', views.about,name='about'),

    path('payments/', views.payment_list, name='payment_list'),
    path('payments/add/', views.add_payment, name='add_payment'),
    path('payment/pdf/', views.payment_pdf, name='payment_pdf'),
]
