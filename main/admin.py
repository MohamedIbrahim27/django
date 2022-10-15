from django.contrib import admin

# Register your models here.

from .models import project ,category
admin.site.register(project)
admin.site.register(category)