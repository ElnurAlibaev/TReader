from django.contrib import admin
from books import models

admin.site.register(models.Book)
admin.site.register(models.Genre)
admin.site.register(models.Tag)
admin.site.register(models.Source)
