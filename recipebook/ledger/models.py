from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", default=None)
    name = models.CharField(max_length=50, unique=True)
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    """An ingredient that can be used in recipes."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:ingredient_detail", args=[self.pk])

class Recipe(models.Model):
    """A recipe that consists of multiple ingredients."""
    name = models.CharField(max_length=255, unique=True)
    
    author = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="recipes", default=None)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[self.pk])

class RecipeIngredient(models.Model):
    """Links an ingredient to a recipe with a given quantity."""
    quantity = models.CharField(max_length=50)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipes"
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients"
    )

    """
    Added so it will appear as 'Recipe Ingredients' instead of 
    'Recipe ingredients' in the admin panel.
    """
    class Meta:
        verbose_name_plural = "Recipe Ingredients"

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} in {self.recipe.name}"
    