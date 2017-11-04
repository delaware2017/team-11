from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    hispanic = models.BooleanField()
    athletic = models.BooleanField()
    arts = models.BooleanField()
    stem = models.BooleanField()
    community_service = models.BooleanField()
    personal_statement = models.BooleanField()
    resume = models.BooleanField()
    transcript = models.BooleanField()

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Nominator(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    #students = models.OneToManyField(Student)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Grader(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    category = models.CharField(max_length=200)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Academics(models.Model):

    id = models.IntegerField(primary_key=True)
    gpa = models.FloatField(default=0.0)
    weighted = models.BooleanField(default=False)



    def __str__(self):
        """this sets the default return for this object"""
        return self.description
