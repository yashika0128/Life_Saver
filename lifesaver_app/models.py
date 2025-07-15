from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Receiver(models.Model):
    patient_name = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    required_blood_group = models.CharField(max_length=5)
    urgency = models.CharField(max_length=20)

    def __str__(self):
        return self.patient_name
