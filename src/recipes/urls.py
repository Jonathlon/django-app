from django.urls import path
from .views import home, records, create_view, about_view
from .views import RecipeListView, RecipesDetailsView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name = 'list'),
    path('detail/<pk>',RecipesDetailsView.as_view(), name = 'detail'),
    path('records/', records, name='records'),
    path('create/', create_view, name='create'),
    path('about/', about_view, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
