from django.db import models

class Donor(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Receiver(models.Model):
    patient_name = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    required_blood_group = models.CharField(max_length=5)
    urgency = models.CharField(max_length=20)

    def __str__(self):
        return self.patient_name
