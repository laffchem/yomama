from django.db import models

# Create your models here.

class Joke(models.Model):
    id = models.AutoField(primary_key=True)
    joke = models.TextField()
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.joke

