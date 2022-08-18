from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.user)
admin.site.register(models.Post)
admin.site.register(models.QAPost)
admin.site.register(models.Subject)
admin.site.register(models.Shop)
