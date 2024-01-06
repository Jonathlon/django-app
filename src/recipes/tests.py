from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name = 'sandwich', cooking_time = 15, 
                              difficulty = 'easy', ingredients = 'bread,ham,cheese', 
                              description = 'this is the best sandwich of your life.' )
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        
        self.assertEqual(field_label, 'name')
