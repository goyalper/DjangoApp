from django.db import models

class Ebook(models.Model):
    title = models.CharField(max_length=50)
    Author = models.CharField(max_length=30)
    price = models.FloatField()
    cover_image = models.CharField(max_length=500000)

    def __str__(self):
        return self.title
    
class CartItems(models.Model):
    title = models.CharField(max_length=50, null = True)
    price = models.FloatField(null=True)