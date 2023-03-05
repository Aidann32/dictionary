from django.contrib import admin

from .models import Meaning, Phrase


@admin.register(Meaning)
class MeaningAdmin(admin.ModelAdmin):
    search_fields = ['meaning', 'meta']
    list_display = ['meaning', 'meta', 'created_at']


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    autocomplete_fields = ["meaning", ]
    search_fields = ['phrase', 'meaning__meaning']
    list_display = ['phrase', 'meaning', 'created_at']
