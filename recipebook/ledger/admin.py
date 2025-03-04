from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name',)
    inlines = [RecipeIngredientInline] 

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('get_ingredient_name', 'quantity', 'get_recipe_name')
    list_filter = ('recipe',)

    @admin.display(description="Ingredient Name")
    def get_ingredient_name(self, obj):
        return obj.ingredient.name  

    @admin.display(description="Recipe")
    def get_recipe_name(self, obj):
        return obj.recipe.name

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)