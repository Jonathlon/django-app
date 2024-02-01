# from django.test import TestCase
# from .models import User, Recipe

# # Create your tests here.

# class UserModelTest(TestCase):
#     def setUpTestData():
#         recipe = Recipe.objects.create(name = 'sandwich', cooking_time = 15, 
#                               difficulty = 'easy', ingredients = 'bread,ham,cheese', 
#                               description = 'this is the best sandwich of your life.' )
#         recipe.save()
#         user = User.objects.create(name = 'jon', saved_recipes = recipe)
#         user.save()
        
#     def test_user_name(self):
#         user = User.objects.get(id=1)
#         field_label = user._meta.get_field('saved_recipes').verbose_name
        
#         self.assertEqual(field_label, 'saved recipes')
