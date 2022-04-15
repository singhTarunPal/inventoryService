
from django.urls import path
from .views import bookinventory
from .views import singlebookinventory

urlpatterns = [
    path('api/bookInventory/', bookinventory, name="bookInventories"),
    path('api/bookInventory/<str:queryparams>', singlebookinventory, name = "bookinventory")
]
