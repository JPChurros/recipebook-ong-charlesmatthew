from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def recipe_list(request):
    recipes = Recipe.objects.all() 
    return render(request, "recipeList.html", {"recipes": recipes})

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

def add_recipe_details(request, num=0):
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
    
    add_ingredient_form = AddIngredientForm()
    add_image_form = AddImageForm()

    if request.method == "POST":
        add_ingredient_form = AddIngredientForm(request.POST)
        add_image_form = AddImageForm(request.POST, request.FILES)

        if add_ingredient_form.is_valid() and add_image_form.is_valid():
            ingredient_data = add_ingredient_form.cleaned_data
            image_data = add_image_form.cleaned_data

            if ingredient_data["name"] != "-----" or ingredient_data["quantity"] != "":
                add_ingredient_form.save()
            
            if image_data["image"]:
                add_image_form.save()
    
    return render(request, "recipeEdit.html", {
        'recipe' : recipe,
        'ingredients' : ingredients,
        'add_ingredient' : add_ingredient_form,
        'add_image' : add_image_form
    })