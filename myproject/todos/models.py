from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

class Student(models.Model):

    id = models.IntegerField(primary_key=true)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    hispanic = models.BooleanField()

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Nominator(models.Model):

    id = models.IntegerField(primary_key=true)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class Grader(models.Model):

    id = models.IntegerField(primary_key=true)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    category = models.CharField(max_length=200)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description
