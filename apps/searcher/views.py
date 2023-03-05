from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Meaning, Phrase


def autocomplete(request):
    if not (request.method == 'POST'):
        return HttpResponseBadRequest()
    body = json.loads(request.body.decode('utf-8'))
    query = body.get('query', '')

    if not query:
        return JsonResponse({'data': ''})

    meanings = []

    if 'mean:' in query:
        query = query.replace('mean:', '')
        if query:
            meanings = Meaning.objects.filter(meaning__icontains=query)
            meanings_list= [f'mean:{meaning.meaning}' for meaning in meanings]
        
    elif 'meta:' in query:
        query = query.replace('meta:', '')
        meanings = Meaning.objects.filter(meta__icontains=query)
        meanings_list= [f'meta:{meaning.meta} - {meaning.meaning} ' for meaning in meanings]
        
    if meanings:
        return JsonResponse({'data': meanings_list})

    if (not 'mean:' in query) and (not 'meta:' in query):
        phrases = Phrase.objects.filter(phrase__icontains=query)
        phrases_list= [phrase.phrase for phrase in phrases]
        return JsonResponse({'data': phrases_list})

    return JsonResponse({'data': ''})


def result(request):
    if not (request.method == 'POST'):
        return HttpResponseBadRequest()

    body = json.loads(request.body.decode('utf-8')) 
    query = body.get('query', '')
    value = body.get('value', '')
    if (not query) and (not value):
        return JsonResponse({'data': ''})

    if ('mean:' in query) or ('meta:' in query):     
        meaning, phrase = None, None
        if 'meta:' in query:
            value = value.replace('meta:', '')
            value = value.split('-')[0].strip()
            
            if Meaning.objects.filter(meta=value).exists():
                meaning = Meaning.objects.filter(meta=value).first()
                phrase = Phrase.objects.filter(meaning=meaning).first()

        else:
            value = value.replace('mean:', '')
            if Meaning.objects.filter(meaning=value).exists():
                meaning = Meaning.objects.filter(meaning=value).first()
                phrase = Phrase.objects.filter(meaning=meaning).first()

        if meaning and phrase:
            data = {'phrase': phrase.phrase.lower(), 'meaning': meaning.meaning.lower(), 'meta': meaning.meta} 
            return JsonResponse({'data': data})
    
    else:
        if Phrase.objects.filter(phrase=value).exists():
            phrase = Phrase.objects.filter(phrase=value).first()

            data = {'phrase': phrase.phrase.lower(), 'meaning': phrase.meaning.meaning.lower(), 'meta': phrase.meaning.meta} 
            return JsonResponse({'data': data})

    return JsonResponse({"data": ''})
