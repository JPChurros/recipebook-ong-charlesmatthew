from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

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

@login_required
def recipe_add(request):
    recipe_form = RecipeForm(request.POST or None)
    ingredient_form = IngredientForm(request.POST or None)
    recipe_ingredient_form = RecipeIngredientForm(request.POST or None)
    
    if request.method == 'POST':
        if 'recipe_form' in request.POST and recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('ledger:recipe_add')
        
        if 'ingredient_form' in request.POST and ingredient_form.is_valid():
            ingredient_form.save()
            return redirect('ledger:recipe_add')

        if 'recipe_ingredient_form' in request.POST and recipe_ingredient_form.is_valid():
            recipe_ingredient_form.save()
            return redirect('ledger:recipe_add')

    return render(request, 'recipeAdd.html', {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'recipe_ingredient_form': recipe_ingredient_form,
    })
