import django.forms as forms
from nominations.models import Nominator, Student, Academics
from django.forms import ModelForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
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

class NominatorForm(ModelForm):
    class Meta:
        model = Nominator
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']
        fields_required = fields


class AcademicForm(ModelForm):
    class Meta:
        model = Academics
        fields = [
        'gpa',
        'weighted',
        'class_rank',
        'class_size',
        'sat_composite',
        'act_composite',
        'number_ap_classes',
        'academic_awards',
        'organizations',
            ]
        fields_required = fields

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )