from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, Ingredient, RecipeImage, Profile
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm, IngredientForm


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'
    success_url = reverse_lazy("ledger:recipe_add")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'recipe_ingredient_form': RecipeIngredientForm(),
            'ingredient_form': IngredientForm(),
        })
        return context

    def form_valid(self, form):
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.author = profile
        return super().form_valid(form)


class RecipeIngredientCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeIngredientForm
    template_name = 'recipe_add_ingredient.html'

    def form_valid(self, form):
        form.save()
        return redirect('ledger:recipe_add')

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_add')


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_add_image.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = self.get_recipe()
        return context

    def form_valid(self, form):
        recipe_image = form.save(commit=False)
        recipe_image.recipe = self.get_recipe()
        recipe_image.save()
        return redirect('ledger:recipe_detail', pk=recipe_image.recipe.pk)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})

    def get_recipe(self):
        return get_object_or_404(Recipe, pk=self.kwargs['pk'])


class RecipeAddIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    template_name = 'recipe_add_ingredient.html'

    def get_success_url(self):
        return reverse("ledger:recipe_add")