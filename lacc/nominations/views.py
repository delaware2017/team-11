from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count

from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from nominations.forms import NominatorForm
from django.http import HttpResponseRedirect

# Create your views here.
from nominations.models import Student, Nominator

def index(request):
    if request.user.is_authenticated():
        return render(request, "nominations/landing.html")
    else:
        return render(request, "nominations/index.html")

@method_decorator(login_required, )
def get_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentForm()
    return render(request, "nominations/student_nominations.html", {'form': form})

#def print_student(request):
#    query_results = Student.objects.all()
#    return render(request, 'vist_applications.html', locals())

class student_list(ListView):
    model = Student

class student_details(DetailView):
    model = Student

class student_create(CreateView):
    model = Student
    fields = ['first_name',
        'last_name',
        'gender',
        'birthday',
        'hispanic',
        'phone',
        'email',
        'school_name',
        'district',
        'county',
        'athletic',
        'arts',
        'stem',
        'community_service']
    fields_required = fields

    def get_success_url(self):
        return reverse('student_details', kwargs={'pk': self.object.pk})

class student_update(UpdateView):
    model = Student
    fields = ['first_name',
        'last_name',
        'gender',
        'birthday',
        'hispanic',
        'phone',
        'email',
        'school_name',
        'district',
        'county',
        'athletic',
        'arts',
        'stem',
        'community_service']
    fields_required = fields

    def get_success_url(self):
        return reverse('student_details', kwargs={'pk': self.object.pk})

class student_delete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

@method_decorator(login_required, name='dispatch')
def landing(request):
    return render(request, "nominations/landing.html")
