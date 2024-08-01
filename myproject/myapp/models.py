from django.db import models
from django.contrib.auth.models import User

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty_of_interest = models.CharField(max_length=50, choices=[
        ('ECE', 'Electrical and Computer Engineering'),
        ('MACS', 'Mathematics and Computer Science'),
        ('INSE', 'Information Systems Engineering'),
        ('Accounting', 'Accounting'),
    ])
    program_of_interest = models.CharField(max_length=50, choices=[
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('Diploma', 'Diploma'),
    ])

    def __str__(self):
        return self.user.username
  
  # myapp/models.py
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.question
    
# myapp/models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)  # New field for location

    def __str__(self):
        return self.title


