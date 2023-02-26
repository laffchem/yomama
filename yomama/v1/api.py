from django.shortcuts import get_object_or_404
from ninja import Router
from .schema import JokeOut
from .models import Joke
from typing import List

router = Router()


# Get Requests


@router.get("/jokes/random/", response=JokeOut)
def get_random_joke(request):
    joke = Joke.objects.all().order_by("?").first()
    return joke


@router.get("/jokes/{category}/", response=List[JokeOut])
def get_joke_list_by_category(request, category: str):
    jokes = Joke.objects.filter(category=category)
    return jokes


@router.get("/jokes/{category}/random/", response=JokeOut)
def get_random_joke_by_category(request, category: str):
    joke = Joke.objects.filter(category=category).order_by("?").first()
    return joke

@router.get("/jokes/{search_term}/")
def get_joke_by_id(request, search_term):
    jokes = Joke.objects.filter(joke__contains=search_term)
    return jokes



