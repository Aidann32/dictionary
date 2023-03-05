from django.core.management.base import BaseCommand, CommandError

from apps.searcher.models import Phrase, Meaning
from apps.searcher.tools import parse_meanings_table, get_meanings, get_phrases 

class Command(BaseCommand):
    help = 'Loads all content from Excel file to DB'

    def handle(self, *args, **options):
        meanings = get_meanings()
        for m in meanings:
            split = m.split('/')
            meaning, meta = split[0], split[1]
            if not Meaning.objects.filter(meaning=meaning, meta=meta).exists():
                Meaning.objects.create(meaning=meaning, meta=meta)

        parsed_table = parse_meanings_table()
        for phrase, meaning in parsed_table.items():
            meaning_str = meaning.split('/')[0]
            if Meaning.objects.filter(meaning=meaning_str).exists():
                meaning_db = Meaning.objects.filter(meaning=meaning_str).first()
                Phrase.objects.create(phrase=phrase, meaning=meaning_db)