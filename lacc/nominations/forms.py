from nominations.models import Nominator, Student, Academics
from django.forms import ModelForm

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
            'academics',
            'overall',
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


