🏥 Hospital Management System

A full-stack Hospital Management System developed using Python and Django with MySQL database.

This project helps manage patients, doctors, appointments, billing, payments, medicines, laboratory tests, and hospital activities from a single web application.

---

🚀 Features

🔐 Authentication
- User Login
- Logout
- Password change
- Wrong password validation
- Protected dashboard
- User profile

👨‍⚕️ Patient Management
- Add Patient
- View Patients
- Search Patient
- Edit Patient
- Delete Patient
- Automatic Patient ID generation
- Patient PDF report
- Patient Excel report

👨‍⚕️ Doctor Management
- Add Doctor
- View Doctors
- Search Doctor
- Edit Doctor
- Delete Doctor
- Automatic Doctor ID generation
- Doctor PDF report
- Doctor Excel report

📅 Appointment Management
- Add Appointment
- View Appointments
- Search Appointments
- Edit Appointment
- Delete Appointment
- Automatic Appointment ID generation
- Appointment PDF report
- Appointment Excel report

💰 Billing Management
- Create Bills
- View Bills
- Search Bills
- Edit Bills
- Delete Bills
- Automatic Bill ID generation
- Billing PDF report
- Billing Excel report

💳 Payment Management
- Add Payment
- View Payments
- Search Payments
- Transaction ID
- Payment Status
- Payment Date
- Payment PDF report

💊 Pharmacy Management
- Add Medicine
- View Medicines
- Search Medicine
- Edit Medicine
- Delete Medicine
- Automatic Medicine ID generation
- Medicine PDF report
- Medicine Excel report

🧪 Laboratory Management
- Add Laboratory Test
- View Laboratory Tests
- Search Tests
- Edit Tests
- Delete Tests
- Automatic Test ID generation
- Laboratory PDF report
- Laboratory Excel report

📊 Dashboard
The dashboard displays:
- Total Patients
- Total Doctors
- Total Appointments
- Total Bills
- Total Medicines
- Total Laboratory Tests
- Appointment information

📝 Activity Log
- Records user login activity
- Displays login time
- Helps track user activity

---

🛠️ Technologies Used

Backend
- Python
- Django

 Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

Database
- MySQL

Reporting
- Report Lab
- OpenPyXL

Authentication
- Django Authentication System

Version Control
- Git
- GitHub

---

📁 Project Structure
hospital/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── hospital/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── patients/
│   ├── migrations/
│   ├── templates/
│   │   └── patients/
│   ├── static/
│   │   └── css/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
└── ...
