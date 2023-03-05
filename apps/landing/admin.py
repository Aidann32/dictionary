from django.contrib import admin
from .models import AboutUsPage


@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    pass
