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
    
    def guess(chosen, comparitor):
        risk = {'Least Concern': 0, 'Near Threatened': 1, 'Vulnerable': 2, 'Endangered': 3, 'Critically Endangered': 4}
        if risk[chosen.status] >= risk[comparitor.status]:
            message = f'Congratulations! You chose {chosen.name}, which has a current status of {chosen.status}. {comparitor.name} only has a status of {comparitor.status}.'
            return {'message': message, 'animal': chosen}
        else:
            message = f'Nice try! {chosen.name} only has a status of {chosen.status}, while {comparitor.name} has a status of {comparitor.status}.'
            return {'message': message, 'animal': comparitor}

class Score(models.Model):
    player_score = 0

    def __str__(self):
        return self.player_score
    
        
