<<<<<<< HEAD
from django import forms
from .models import Species

class AnimalForm(forms.ModelForm):
	 class Meta:
	 	model = Animal
	 	fields = ["image", "name", "status", "population", "author", "image_license", "license_url", "image_url"]
=======
from django.forms import ModelForm
from django import forms
from .models import Animal

"""
class GuessForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['chosen', 'comparitor']
"""
class GuessForm(forms.Form):
    chosen_name = forms.CharField(label='chosen_name', max_length=200, widget=forms.HiddenInput())
    comparitor_name = forms.CharField(label='comparitor_name', max_length=200, widget=forms.HiddenInput())
>>>>>>> origin/main
