from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    timeRequired = models.CharField(max_length=30)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.author}"
