from django.urls import path
from . import views
from .api import router
from .private_api import private_router

urlpatterns = [
    path("", router),
    path("/internal", private_router)
]

