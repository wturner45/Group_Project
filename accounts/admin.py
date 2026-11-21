from django.contrib import admin

from .models import OwnerProfile, Pet


admin.site.register(OwnerProfile)
admin.site.register(Pet)
