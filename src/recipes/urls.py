from django.urls import path
from .views import home, records, create_view, about_view
from .views import RecipeListView, RecipesDetailsView

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name = 'list'),
    path('detail/<pk>',RecipesDetailsView.as_view(), name = 'detail'),
    path('records/', records, name='records'),
    path('create/', create_view, name='create'),
    path('about/', about_view, name='about'),
]