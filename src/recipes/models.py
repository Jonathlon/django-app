from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length = 120)    
    cooking_time = models.IntegerField(help_text = 'in mintues', default = 0 )    
    difficulty = models.CharField(max_length = 13)    
    ingredients = models.CharField(max_length = 300)    
    description = models.TextField()
    
    def __str__(self):
        return str(self.name)
