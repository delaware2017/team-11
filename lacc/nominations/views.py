from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count

from django.contrib.auth.models import User

# Create your views here.

def index(request):
#    todos_by_user = User.objects.annotate(num_todos=Count('todo'))
#    context = {
#        'todos_by_user': todos_by_user
#    }
    return render(request, "nominations/index.html")

#def landing(request):
#    return render(request, "/landing.html")

#@method_decorator(login_required, name='dispatch')  # Require login
