# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields if necessary

class AdmissionDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    # Add other fields as necessary
    
    def __str__(self):
        return self.name
    
class StudentMarks(models.Model):
    student_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()

    def __str__(self):
        return self.student_name