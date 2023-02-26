from django.shortcuts import get_object_or_404
from ninja import Router
from .schema import JokeIn
from .models import Joke
from ninja.security import django_auth

private_router = Router()

# Post Requests

@private_router.post("/joke/", auth=django_auth)
def create_new_joke_by_category(request, payload: JokeIn):
    joke = Joke.objects.create(**payload.dict())
    return {"id": joke.joke}


# Put Request

@private_router.put("/joke/{joke_id}", auth=django_auth)
def edit_joke_by_id(request, joke_id: int, payload: JokeIn):
    joke = get_object_or_404(Joke, id=joke_id)
    joke.joke = payload.joke
    joke.save()
    return {"success": True}


# Delete Request

@private_router.delete("/joke/{joke_id}", auth=django_auth)
def delete_joke_by_id(request, joke_id: int, payload: JokeIn):
    joke =  get_object_or_404(Joke, id=joke_id)
    deleted_joke = joke.joke
    joke.delete()
    return {"success": f"{deleted_joke} was deleted"}