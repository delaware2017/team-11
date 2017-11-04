from django.forms import ModelForm
from nominations.models import Nominator

class NominatorForm(ModelForm):
    class Meta:
        model = Nominator
        fields = ['first_name', 'last_name', 'email', 'phone']
