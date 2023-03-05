from django.urls import path
from .views import about_us, main 

urlpatterns = [
    path('', main, name="main_page"),
    path('about/', about_us, name='about'),
]