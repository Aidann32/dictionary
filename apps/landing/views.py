from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import AboutUsPage


@login_required(login_url='login')
def main(request):
    return render(request, 'landing/main.html', {})


@login_required(login_url='login')
def about_us(request):
    pages = AboutUsPage.objects.filter(is_active=True)
    
    if pages:
        page = pages.last()
        return render(request, "landing/about.html", {'page': page})
    
    return render(request, "landing/about.html")
