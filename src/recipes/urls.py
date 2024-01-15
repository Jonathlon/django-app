from django.urls import path
from .views import home
from .views import RecipeListView, RecipesDetailsView

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name = 'list'),
    path('list/<pk>',RecipesDetailsView.as_view(), name = 'detail'),
]