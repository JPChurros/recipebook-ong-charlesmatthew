from django.db import models
from datetime import datetime
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[self.id])

class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.id])

class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=100)
    Ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    Recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients'
    )

    def __str__(self):
        return f"{self.Quantity} of {self.Ingredient.name} for {self.Recipe.name}"

# Create your models here.
