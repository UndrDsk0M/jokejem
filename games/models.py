from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    emojie = models.CharField(max_length=5, null=True)
    description = models.TextField()
    keywords = models.TextField()
    image = models.ImageField(upload_to='img/category/')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.keywords = self.keywords.split()
        super().save(*args, **kwargs)
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    emojie_1 = models.CharField(max_length=5, default="💰")
    description = models.TextField()
    keywords = models.TextField()
    image = models.ImageField(upload_to='img/game/')
    price = models.CharField(max_length=50)
    emojie_2 = models.CharField(max_length=5, default="💵")
    category = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.keywords = self.keywords.split()
        super().save(*args, **kwargs)