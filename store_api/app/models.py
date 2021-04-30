from django.db import models
from datetime import date
from dotenv import dotenv_values
from django.core.serializers import serialize


class Order(models.Model):
    """Define all args about Order class"""
    STATUS_OPTIONS = [
        ('CRT', 'CREATED'),
        ('PD', 'PAYED'),
        ('RD', 'REJECTED'),
    ]
    costumer_name = models.CharField(max_length=80, null=False)
    costumer_email = models.EmailField(max_length=120, null=False)
    costumer_mobile = models.CharField(max_length=40, null=False)
    status = models.CharField(max_length=3, choices=STATUS_OPTIONS, default="CRT", null=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'order'

    def serializer(self):
        """method to serialize to json"""
        return {
            f'{ key }': value for key, value in self.__dict__.items()
            if key != '_state'
        }

    def __str__(self):
        return f" {self.id} | {self.costumer_name} "
