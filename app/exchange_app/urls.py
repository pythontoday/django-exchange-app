from django.urls import path
from .views import exchange

urlpatterns = [
    path('', exchange)
]