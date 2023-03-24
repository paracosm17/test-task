from django.db import models
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    owners = models.ManyToManyField('CustomUser', through='Ownership')


class CustomUser(AbstractUser):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        related_name = "User"
        related_name_plural = "Users"


class Ownership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'car')
