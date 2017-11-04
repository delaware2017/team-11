from django.contrib import admin

# Register your models here.
from .models import Nominator
from .models import Student
from .models import Grader
from .models import Academics

admin.site.register(Nominator)
