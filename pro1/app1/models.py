from django.db import models


class Create(models.Model):
    s_choice = [('yes', 'YES'), ('no', 'NO')]
    car_name = models.CharField(max_length=20)
    car_price = models.IntegerField()
    sunroof = models.CharField(max_length=10, choices=s_choice)
    purchase_date = models.DateField()
