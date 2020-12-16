from django.contrib import admin
from .models import Article, Reporter, Place, Restaurant

# Register your models here.

admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(Place)
admin.site.register(Restaurant)