from django.db import models

class Order(models.Model):
    user = models.ForeignKey()
    product = models.ForeignKey()
    craate_data = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)
