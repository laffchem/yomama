from django.shortcuts import render
from v1.models import Joke

def home(request):
    categories = Joke.objects.values_list('category', flat=True).distinct()
    context = {
        "context": categories
    }
    return render(request, 'index.html', context)


def api_docs(request):
    return render(request, 'api-docs.html')

