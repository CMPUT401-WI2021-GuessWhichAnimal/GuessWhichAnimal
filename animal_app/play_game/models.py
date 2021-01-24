from django.db import models

class animal(models.Model);
	name=models.CharField(max_length=40)
	image=models.ImageField(blank=True, null=True)

def __str__(self):
	return self.name
