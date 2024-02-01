from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm 

# Create your tests here.

from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cooking_time = recipe.cooking_time
        self.assertEqual(recipe_cooking_time, 25)

    def test_ingredients_list(self):
        recipe = Recipe.objects.get(id=1)
        recipe_ingredients = recipe.ingredients
        self.assertEqual(recipe_ingredients, 'bread,ham,cheese,')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calc_difficulty(), 'Intermediate')

class RecipeFormTestCase(TestCase):
    def test_valid_form(self):
        data = {
            "name": "Spaghetti Bolognese",
            "cooking_time": 25,
            "ingredients": "Spaghetti, Beef Mince, Tomato Paste, Tomato Sauce, Onion",
        }
        form = RecipeSearchForm(data=data)
        self.assertTrue(form.is_valid())