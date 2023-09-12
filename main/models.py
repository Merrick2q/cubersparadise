from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='items/')  # Define the upload_to path

    def __str__(self):
        return self.name
