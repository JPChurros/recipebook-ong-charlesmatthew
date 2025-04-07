from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:num>/', recipe_detail, name='recipe_detail'),
    path('recipe/<int:num>/edit/', add_recipe_details, name='add_recipe_details'),
]

app_name = "ledger"