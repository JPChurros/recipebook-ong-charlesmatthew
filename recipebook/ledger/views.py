from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all() 
    return render(request, "recipeList.html", {"recipes": recipes})

@login_required
def recipe_detail(request, num=1):
    try:
        recipe = Recipe.objects.get(id=num)
        ingredients = recipe.recipe_ingredients.all()

        ri = []

        ingredients = [
            {"name": ri.Ingredient.name, "quantity": ri.Quantity}
            for ri in ingredients
        ]
    except Recipe.DoesNotExist:
        recipe = None
        ingredients = []

    return render(request, 'recipeDetails.html', {
        'recipe': recipe,
        'ingredients' : ingredients
    })
