from django.db import models
class Patient(models.Model):
    patient_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=15)
    disease=models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
class Doctor(models.Model):
    doctor_id=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Appointment(models.Model):
    appointment_id = models.CharField(max_length=10, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    def __str__(self):
        return self.appointment_id

class Billing(models.Model):
    bill_id = models.CharField(max_length=10, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_fee = models.DecimalField(max_digits=10, decimal_places=2)
    test_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('Paid', 'Paid'),
            ('Unpaid', 'Unpaid'),
        ],
        default='Unpaid'
    )

    def __str__(self):
        return self.bill_id

class Medicine(models.Model):
    medicine_id = models.CharField(max_length=10, unique=True)
    medicine_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.medicine_name

class Laboratory(models.Model):
    test_id = models.CharField(max_length=10, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    test_date = models.DateField()
    result = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.test_id

class ActivityLog(models.Model):
    username = models.CharField(max_length=100)
    action = models.CharField(max_length=255)
    action_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + "_"+self.action

class Payment(models.Model):
    bill = models.ForeignKey(
        'Billing',
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    transaction_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bill} - {self.amount} - {self.status}"