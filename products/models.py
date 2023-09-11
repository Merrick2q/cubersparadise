from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, default='Mscube MS3X')
    quantity = models.IntegerField(default=50)
    description = models.TextField(default='Puzzle rubik flagship oleh Mscube')

    def __str__(self):
        return self.name
