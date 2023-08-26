from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    category = models.ForeignKey(Category, related_name='vehicles', on_delete=models.CASCADE)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    power_hp = models.IntegerField()
    year = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='vehicle_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='vehicles', on_delete=models.CASCADE)

    def __str__(self):
        return self.make + ' ' + self.model