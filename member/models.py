from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)