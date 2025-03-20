from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name="recipe_list"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),  
    path('logout/', LogoutView.as_view(), name="logout"),  
]

app_name = 'ledger'