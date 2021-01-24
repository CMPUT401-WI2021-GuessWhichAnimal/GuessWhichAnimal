from django.shortcuts import render
from .models import Animal
from .forms import GuessForm
import random

def field(request):
	animals = Animal.objects.all()
	animal1 = random.choice(animals)
	while True: # Pick animals until we have 2 that are not the same status
		animal2 = random.choice(animals)
		if animal1.status != animal2.status:
			break
	form1 = GuessForm(initial={'chosen_name': animal1.name, 'comparitor_name': animal2.name})
	form2 = GuessForm(initial={'chosen_name': animal2.name, 'comparitor_name': animal1.name})
	return render(request, 'field.html', {'animal1': animal1, 'animal2': animal2, 'form1': form1, 'form2': form2})

def guess(request):
	if request.method == 'POST':
		form = GuessForm(request.POST)
		chosen_name = form.data['chosen_name']
		comparitor_name = form.data['comparitor_name']
		animals = Animal.objects.all()
		chosen = next(obj for obj in animals if obj.name == chosen_name)
		comparitor = next(obj for obj in animals if obj.name == comparitor_name)
		result = Animal.guess(chosen, comparitor)
		return render(request, 'guess.html', {'message': result['message'], 'animal': result['animal']})
