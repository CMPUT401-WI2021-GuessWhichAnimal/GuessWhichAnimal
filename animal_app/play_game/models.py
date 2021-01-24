from django.db import models



class Animal(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    population = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image_license = models.CharField(max_length=200)
    license_url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Score(models.Model):
    player_score = 0

    def __str__(self):
        return self.player_score