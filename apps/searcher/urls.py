from django.urls import path
from .views import autocomplete, result

urlpatterns = [
    path('', autocomplete, name='autocomplete'),
    path('result/', result, name='result')
]