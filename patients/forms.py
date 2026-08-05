from django import forms
from.models import Patient
from .models import Doctor
from .models import Appointment
from .models import Billing
from .models import Medicine
from .models import Laboratory
from .models import Payment
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=[
            'name',
            'age',
            'gender',
            'phone',
            'disease'
        ]
class DoctorForm(forms.ModelForm):
        class Meta:
            model=Doctor
            fields=[
                'name',
                'specialization',
                'phone',
                'email'
            ]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'status']


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = [
            'patient',
            'doctor',
            'consultation_fee',
            'medicine_fee',
            'test_fee',
            'total_amount',
            'payment_status'
        ]


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'medicine_name',
            'company',
            'price',
            'quantity',
            'expiry_date'
        ]


class LaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = [
            'patient',
            'test_name',
            'test_date',
            'result',
            'amount'
        ]

        widgets = {
            'test_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields ='__all__'

        widgets = {
            'bill': forms.Select(attrs={
                'class': 'form-control'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),

            'transaction_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter transaction ID'
            }),

            'status': forms.Select(
                choices=[
                    ('Pending','Pending'),
                    ('Completed','Completed'),
                    ('Failed','Failed'),],
                attrs={
                    'class':'form-control'
                }
            ),
        }   