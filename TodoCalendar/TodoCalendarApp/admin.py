from django.contrib import admin
from . import models as db

# Register your models here.

admin.site.register(db.User)
admin.site.register(db.Todo)
admin.site.register(db.Labels)