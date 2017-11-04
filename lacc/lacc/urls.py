"""lacc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from nominations.forms import NominatorForm, StudentForm
from nominations.views import student_list

urlpatterns = [
    url(r'^accounts/login/', LoginView.as_view(), name="user_login"),
    url(r'^accounts/logout/', LogoutView.as_view(), name="user_logout"),
    url(r'^accounts/register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class = UserCreationForm,
            success_url='/'
    )),
    url(r'^student/create/', CreateView.as_view(
            template_name='nominations/student_nominations.html',
            success_url='/',
            form_class=StudentForm
    )),
    url(r'^students/', student_list.as_view(
            
    )),

    url(r'^admin/', admin.site.urls),
    url(r'^', include('nominations.urls')),
]
