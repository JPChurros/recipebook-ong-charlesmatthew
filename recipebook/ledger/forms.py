from django import forms
from .models import Ingredient, RecipeImage

class AddIngredientForm(forms.Form):
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        empty_label="-----",
        widget=forms.Select
    )
    quantity = forms.CharField(max_length=100)

class AddImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'descripton']