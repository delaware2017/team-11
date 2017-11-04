from django.db import models
import datetime
# Leverage Django's built-in User models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(default="null", max_length=30)
    last_name = models.CharField(default="null", max_length=30)
    email = models.CharField(default="null", max_length=200)
    phone = models.CharField(default="null", max_length=10)
    hispanic = models.BooleanField(default=False)
    birthday = models.DateField(default=datetime.datetime.now)
    school_name = models.CharField(default="null", max_length=300)
    district = models.CharField(default="null", max_length=50)
    county = models.CharField(default="null", max_length=100)
    athletic = models.BooleanField(default=False)
    arts = models.BooleanField(default=False)
    stem = models.BooleanField(default=False)
    community_service = models.BooleanField(default=False)
    personal_statement = models.BooleanField(default=False)
    resume = models.BooleanField(default=False)
    transcript = models.BooleanField(default=False)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Nominator(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(default="null", max_length=30)
    last_name = models.CharField(default="null", max_length=30)
    email = models.CharField(default="null", max_length=200)
    password = models.CharField(default="null", max_length=200)
    phone = models.CharField(default="null", max_length=10)
    #students = models.OneToManyField(Student)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Grader(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(default="null", max_length=30)
    last_name = models.CharField(default="null", max_length=30)
    email = models.CharField(default="null", max_length=200)
    phone = models.CharField(default="null", max_length=10)
    category = models.CharField(default="null", max_length=200)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Academics(models.Model):

    id = models.IntegerField(primary_key=True)
    gpa = models.FloatField(default=0.0)
    weighted = models.BooleanField(default=False)
    class_rank = models.IntegerField(default=0)
    class_size = models.IntegerField(default=0)
    sat_composite = models.IntegerField(default=0)
    sat_reading = models.IntegerField(default=0)
    sat_writing = models.IntegerField(default=0)
    sat_math = models.IntegerField(default=0)
    act_composite = models.IntegerField(default=0)
    act_reading = models.IntegerField(default=0)
    act_english = models.IntegerField(default=0)
    act_math = models.IntegerField(default=0)
    act_science = models.IntegerField(default=0)
    act_writing = models.IntegerField(default=0)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Art(models.Model):

    id = models.IntegerField(primary_key=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class STEM(models.Model):

    id = models.IntegerField(primary_key=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description
