from django.shortcuts import render, redirect
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

    add_image_form = AddImageForm()

    if request.method == "POST":
        add_image_form = AddImageForm(request.POST, request.FILES)
        if add_image_form.is_valid():
            image = add_image_form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect("ledger:recipe_detail", num=num)


    return render(request, 'recipeDetails.html', {
        'recipe' : recipe,
        'ingredients' : ingredients,
        'add_image_form' : add_image_form,
    })