from django.shortcuts import render
from django.http import HttpResponse
from v1.models import Joke


# Create your views here.
def htmx_random_joke(request):
    joke = Joke.objects.all().order_by("?").first()
    return HttpResponse(f"<td class='jokes'><p>{joke}</p></td>")


def htmx_jokes_by_category(request):
    category = request.POST.get('joke-category')
    jokes = Joke.objects.filter(category=category)
    # for joke in jokes:
    #     return HttpResponse(f"<td class='jokes'>{joke}</td>)")
    return HttpResponse(jokes)


def htmx_joke_by_category(request):
    category = request.POST.get('joke-category')
    joke = Joke.objects.filter(category=category).order_by("?").first()
    return HttpResponse(joke)


def api_docs(request):
    pass