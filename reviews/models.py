from django.db import models

# Create your models here.

class Reviews(models.Model):
    #film = models.CharField(' Film ', max_length=50)
    reviews = models.TextField(' Reviews ')
    #name = models.TextField(' Name film ')
    #name = models.CharField(' Film ', max_length=50)
    # grade = models.IntegerField(' Grade ')
    # color = models.IntegerField(' Neg or Pos ')

    def __str__(self):
        return self.reviews
