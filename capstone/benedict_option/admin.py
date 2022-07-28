from django.contrib import admin

# Register your models here.

from .models import User, Liturgy, Group

# Register your models here.
admin.site.register(User)
admin.site.register(Liturgy)
admin.site.register(Group)
