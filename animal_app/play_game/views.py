from django.shortcuts import render

def field(request):
	return render(request, 'field.html', {})
