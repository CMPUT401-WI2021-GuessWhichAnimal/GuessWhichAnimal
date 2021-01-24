from django.shortcuts import render
from .models import Animal
import random

def field(request):
	animals = Animal.objects.all()
	animal1 = random.choice(animals)
	while True: # Pick animals until we have 2 that are not the same status
		animal2 = random.choice(animals)
		if animal1.status != animal2.status:
			break
	return render(request, 'field.html', {'animal1': animal1, 'animal2': animal2})
