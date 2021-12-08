from django.db import models


class Currency(models.Model):
    Bill = "Bill"
    Coin = "Coin"

    TYPE_CHOICES = [
        (Bill, "Bill"),
        (Coin, "Coin")
    ]

    book = models.IntegerField(null=True, default=None)
    page = models.IntegerField(null=True, default=None)
    row = models.IntegerField(null=True, default=None)
    column = models.IntegerField(null=True, default=None)
    currency = models.CharField(max_length=100, blank=True, default="")
    value = models.IntegerField(null=True, default=None)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    country = models.CharField(max_length=2, blank=True, default="")

    # Audit Fields.
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)
