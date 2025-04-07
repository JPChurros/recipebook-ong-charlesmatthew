from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:num>/', recipe_detail, name='recipe_detail'),
    path('recipe/add/', recipe_add, name='recipe_add'),
]

app_name = "ledger"