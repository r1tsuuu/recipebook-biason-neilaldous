from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    name = models.CharField(max_length=50, unique=True)
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:ingredient_detail", args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipes")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    class Meta:
        verbose_name_plural = "Recipe Ingredients"

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} in {self.recipe.name}"


class RecipeImage(models.Model):
    image = models.ImageField(null=False, upload_to="recipe_images/")
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Image for {self.recipe.name}"

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.recipe.pk)])