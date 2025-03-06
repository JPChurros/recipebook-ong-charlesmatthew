from django.urls import path
from .views import *

urlpatterns = {
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:num>/', recipeListTemplate, name='recipeListTemplate'),
    path('ingredient/<int:id>/', recipe_detail, name='recipe_detail')
}

app_name = "ledger"