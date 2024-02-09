from django import forms
from .models import *

class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'


class WhiskyForm(forms.ModelForm):
    class Meta:
        model = Whisky
        fields = '__all__'
        