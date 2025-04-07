from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('recipes/add/ingredient/', views.RecipeAddIngredientView.as_view(), name='recipe_add_ingredient'),
    path('recipes/list/', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipes/add/recipe-ingredient/', views.RecipeIngredientCreateView.as_view(), name='recipe_add_recipe_ingredient'),
    
    path('recipes/add/', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/<int:pk>/add_image/', views.RecipeImageCreateView.as_view(), name='recipe_add_image'),
    
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe_detail"),
    
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


app_name = "ledger"