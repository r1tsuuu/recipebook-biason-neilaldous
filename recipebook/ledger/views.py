from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
    """Displays the list of all recipes"""
    model = Recipe
    template_name = "recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(DetailView):
    """Displays detailed information of a recipe."""
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"