from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def recipe_list(request):
    recipes = Recipe.objects.all() 
    return render(request, "recipeList.html", {"recipes": recipes})

def recipe_detail(request, num=1):
    try:
        recipe = Recipe.objects.get(id=num)
        ingredients = recipe.recipe_ingredients.all()

        ingredients = [
            {"name": ri.ingredient.name, "quantity": ri.quantity}
            for ri in ingredients
        ]
    except Recipe.DoesNotExist:
        recipe = None
        ingredients = []

    return render(request, 'recipeDetails.html', {
        'recipe': recipe,
        'ingredients' : ingredients
    })

# Create your views here.
