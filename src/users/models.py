from django.db import models
from recipes.models import Recipe

# Create your models here.
class User(models.Model):
    name = models.CharField(help_text = 'please enter your name....', max_length = 30)    
    saved_recipes = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    
    def __str__(self):
        return f" {self.name}, saved recipes: {self.saved_recipes.name}"
