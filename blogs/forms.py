from django.forms import ModelForm
from .models import room
from .models import mail
class roomform(ModelForm):
	class Meta:
         model=room
         fields='__all__'
class mailform(ModelForm):
	class Meta:
         model=mail
         fields='__all__'
         