from django import forms
from .models import Species

class AnimalForm(forms.ModelForm):
	 class Meta:
	 	model = Animal
	 	fields = ["image", "name", "status", "population", "author", "image_license", "license_url", "image_url"]