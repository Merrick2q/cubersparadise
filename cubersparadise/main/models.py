from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name
