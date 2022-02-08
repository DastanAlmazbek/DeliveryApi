from django.db import models
from django.contrib.auth import get_user_model
from account.models import User


class Order(models.Model):
    title = models.CharField(max_length=50,
                             unique=True)
    order_info = models.TextField()
    images = models.ImageField(upload_to='pics',
                              null=True,
                              blank=True,)

    def __str__(self):
        return self.title

    # rating = models.PositiveIntegerField(default=1, null=True, blank=True)


class OrderReview(models.Model):
    title = models.ForeignKey(Order,
                             on_delete=models.CASCADE,
                             related_name='titles',)
    name = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews', null=True)

    text = models.TextField()
    rating = models.PositiveIntegerField(default=1, null=True, blank=True)

