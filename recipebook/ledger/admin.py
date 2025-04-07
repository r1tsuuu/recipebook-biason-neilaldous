from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    inlines = [RecipeIngredientInline, RecipeImageInline]

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('get_ingredient_name', 'quantity', 'get_recipe_name')
    list_filter = ('recipe',)
    search_fields = ('ingredient__name', 'recipe__name')
    list_display_links = ('get_ingredient_name', 'get_recipe_name')

    @admin.display(description="Ingredient Name")
    def get_ingredient_name(self, obj):
        return obj.ingredient.name  

    @admin.display(description="Recipe")
    def get_recipe_name(self, obj):
        return obj.recipe.name

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    
    def __str__(self):
        return self.username


admin.site.unregister(User)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(User, CustomUserAdmin)