from django import forms
from django.db import models
from django.forms import ModelForm

CHART_CHOICES = (
    ('#1', 'bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length = 120)
    chart_type = forms.ChoiceField(choices = CHART_CHOICES)


class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    cooking_time = forms.IntegerField(help_text='in minutes', required=False)
    ingredients = forms.CharField(max_length=300, required=False)
    description = forms.CharField(max_length=500, required=False)
    pictures = forms.ImageField(required=False) 
    

    
