from django.conf import settings
from django.db import models


class OwnerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owner_profile",
    )
    address = models.TextField(max_length=500)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.user.get_full_name() or self.user.get_username()


class Pet(models.Model):
    owner = models.ForeignKey(
        OwnerProfile,
        on_delete=models.CASCADE,
        related_name="pets",
    )
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=60)

    def __str__(self):
        return self.name
