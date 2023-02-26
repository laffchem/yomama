from django.urls import path
from . import views

urlpatterns = [
    path("random_joke/", views.htmx_random_joke, name='random-joke'),
    path("random_jokes_category/", views.htmx_jokes_by_category, name='random-jokes-category'),
    path("random_joke_category/", views.htmx_joke_by_category, name='random-joke-category'),
]