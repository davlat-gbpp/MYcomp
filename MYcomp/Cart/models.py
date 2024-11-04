from django.db import models

class Cart(models.Model):
    user = models.ForeignKey()
    product = models.ManyToManyField()
