from django.contrib import admin
from .models import WatchList,StreamPlatform,Review

# Register your models here.
models = (WatchList,StreamPlatform,Review)
for m in models:
    admin.site.register(m)