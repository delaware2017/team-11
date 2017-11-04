from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count

from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from nominations.forms import NominatorForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return render(request, "nominations/landing.html")
    else:
        return render(request, "nominations/index.html")

def get_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentForm()
    return render(request, "nominations/student_nominations0.html", {'form': form})

def print_student(request):
    query_results = Student.objects.all()
    return render(request, 'vist_applications.html', locals())

@method_decorator(login_required, name='dispatch')
def landing(request):
    return render(request, "nominations/landing.html")


