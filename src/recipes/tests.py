from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm 

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name="Pizza", ingredients="Dough, Tomato Paste, Mushrooms",
                              cooking_time=20, description="The best Pizza ever")

    
    def test_description(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.description,
                         "The best Pizza ever")

    def test_name_max_length(self):
        recipe = Recipe.objects.get(name="Pizza")
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(name="Pizza")
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 300)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), "/list/1")


class RecipeFormTest(TestCase):
    def test_recipe_search_form_valid(self):
        form = RecipeSearchForm(data={'chart_type': '#1', 'recipe_name': 'Pizza'})
        self.assertTrue(form.is_valid())