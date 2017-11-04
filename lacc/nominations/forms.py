from nominations.models import Nominator
from django import forms
from django.forms import ModelForm

class NominatorForm(ModelForm):
    class Meta:
        model = Nominator
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']
        fields_required = fields
