from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
   
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(DetailView):
   
    model = Recipe
    template_name = "recipe_detail.html"


def recipe_list(request):

    recipes = Recipe.objects.all()
    ctx = {'recipes' : recipes}
    return render(request, 'recipe_list.html', ctx)


def recipe_detail(request,pk):
   
    ctx = {'recipe' : Recipe.objects.get(pk=pk)}
    return render(request,'recipe_detail.html', ctx)