from django.db import models
import datetime
# Leverage Django's built-in User models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Nominator(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(default="", max_length=30)
    last_name = models.CharField(default="", max_length=30)
    email = models.CharField(default="", max_length=200)
    password = models.CharField(default="", max_length=200)
    phone = models.CharField(default="", max_length=10)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

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
    gender = models.CharField(default="null", choices=GENDER, max_length = 7)
    birthday = models.DateField(default=datetime.datetime.now)
    school_name = models.CharField(default="null", max_length=300)
    district = models.CharField(default="null", max_length=50)
    county = models.CharField(default="null", max_length=100)
    academics = models.BooleanField(default=False)
    athletic = models.BooleanField(default=False)
    arts = models.BooleanField(default=False)
    stem = models.BooleanField(default=False)
    community_service = models.BooleanField(default=False)
    overall = models.BooleanField(default=False)
    personal_statement = models.BooleanField(default=False)
    resume = models.BooleanField(default=False)
    transcript = models.BooleanField(default=False)
    nominator = models.ForeignKey(Nominator, default=0)
    password = models.CharField(default="null", max_length = 100)

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
    act_composite = models.IntegerField(default=0)
    number_ap_classes = models.IntegerField(default=0)
    academic_awards = models.CharField(default="null", max_length = 500)
    organizations = models.CharField(default="null", max_length = 500)


    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Art(models.Model):

    id = models.IntegerField(primary_key=True)
    portfolio_link = models.CharField(default="null", max_length = 500)
    file_upload = models.CharField(default="null", max_length = 300)
    honors_awards = models.CharField(default="null", max_length = 500)
    organizations = models.CharField(default="null", max_length = 500)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class STEM(models.Model):

    id = models.IntegerField(primary_key=True)
    organizations = models.CharField(default="null", max_length = 500)
    honors_awards = models.CharField(default="null", max_length = 500)
    projects = models.CharField(default="null", max_length = 500)
    coursework = models.CharField(default="null", max_length = 500)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Athletics(models.Model):

    id = models.IntegerField(primary_key=True)
    organizations = models.CharField(default="null", max_length = 500)
    honors_awards = models.CharField(default="null", max_length = 500)
    leadership = models.CharField(default="null", max_length = 500)
    academic_achievement = models.CharField(default="null", max_length = 500)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class CommunityService(models.Model):

    id = models.IntegerField(primary_key=True)
    organizations = models.CharField(default="null", max_length = 500)
    service_hours = models.IntegerField(default=0)
    service_hour_proof = models.CharField(default="null", max_length = 500)
    honors_awards = models.CharField(default="null", max_length = 500)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description
