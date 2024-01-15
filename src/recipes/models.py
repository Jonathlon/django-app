from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length = 120)    
    cooking_time = models.IntegerField(help_text = 'in mintues', default = 0 )    
    ingredients = models.CharField(max_length = 300)    
    description = models.TextField()
    pictures = models.ImageField(upload_to = 'recipes', default = 'no_picture.jpg')

    def calc_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'
        return difficulty
    
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})
