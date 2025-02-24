from django.urls import path
from .views import *

urlpatterns = {
    path('recipes/list/', recipe_list, name='recipe_list'),
}

app_name = "ledger"