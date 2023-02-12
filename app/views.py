from .models import Url, Text
from django.http import Http404
from django.shortcuts import render, HttpResponse
from random import choice
from spyntax import *


# Create your views here.


def index(request):
    try:
        urls = Url.objects.order_by("-pub_date")
        context = {"urls": urls}
    except Url.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, "index.html", context)


def pages(request, url):
    context = {}
    if "." in url:
        return render(request, "index.html", {"urls": ""})
    try:
        url = Url.objects.filter(url=url)[0]
        text = choice([i.text for i in Text.objects.filter(url=url)])
        text = choice(generate_all_sentences(text))
        context = {"text": text}
    except Url.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, "page2.html", context)


# Url.objects.filter(url=url)[0].textc
