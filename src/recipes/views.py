from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm, CreateRecipeForm
from .utils import get_recipename_from_id, get_chart
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe    
    template_name = 'recipes/recipes_list.html'
    
class RecipesDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe    
    template_name = 'recipes/recipes_details.html'

def about_view(request):
    return render(request, 'recipes/about.html')

@login_required
def create_view(request):
    create_form = CreateRecipeForm(request.POST or None, request.FILES)
    name = None
    cooking_time = None
    ingredients = None
    description = None
    pictures = None

    if request.method == 'POST':

        try:
            recipe = Recipe.objects.create(
                name = request.POST.get('name'),
                cooking_time = request.POST.get('cooking_time'),
                ingredients = request.POST.get('ingredients'),
                description = request.POST.get('description'),
                pictures = request.FILES.get('picutres', 'no_picture.jpg')
            )

            recipe.save()

           

        except:
            print('Error!!!')

    context = {
        'create_form': create_form,
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'description': description,
        'pictures': pictures,
    }

    return render(request, 'recipes/create.html', context)

@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    chart = None
    
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')    
        chart_type = request.POST.get('chart_type')    
        print(recipe_name, chart_type)
        
        qs = Recipe.objects.filter(name=recipe_name)
        if qs:
            recipe_df = pd.DataFrame(qs.values())     
            recipe_df['id'] = recipe_df['id'].apply(get_recipename_from_id)               
            chart = get_chart(chart_type, recipe_df, labels=recipe_df['cooking_time'].values)             
            recipe_df = recipe_df.to_html()
            

    context = {
        'form' : form,
        'recipe_df' : recipe_df,
        'chart' : chart
    }
            
    return render(request, 'recipes/records.html', context)