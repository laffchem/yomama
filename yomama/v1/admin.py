from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Joke


# Register your models here.

# class JokeAdmin(admin.ModelAdmin):
#     list_display = ('joke', 'category')

@admin.register(Joke)
class JokeAdmin(ImportExportModelAdmin):
    list_display = ("id", "joke", "category")
    pass
