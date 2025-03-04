from django.shortcuts import render
from .models import Recipe, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    
    recipe_data = [
        {
            "name": recipe.name,
            "link": f"/recipe/{recipe.id}",
            "title": "Recipe Book"
        }
        for recipe in recipes
    ]

    ctx = {"recipes": recipe_data}
    return render(request, "recipe_list.html", ctx)

def recipe_1(request):
    recipe = Recipe.objects.get(name="Recipe 1") 
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    ctx = {
        "recipe": recipe,
        "ingredients": ingredients,
        "link": "/recipes/list",
        "title": recipe.name
    }

    return render(request, "recipe.html", ctx)

def recipe_2(request):

    recipe = Recipe.objects.get(name="Recipe 2") 
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    ctx = {
        "recipe": recipe,
        "ingredients": ingredients,
        "link": "/recipes/list",
        "title": recipe.name
    }

    return render(request, "recipe.html", ctx)
