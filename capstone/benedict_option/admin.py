from django.contrib import admin

# Register your models here.

from .models import User,Prayer, Group

# Register your models here.
admin.site.register(User)
admin.site.register(Prayer)
admin.site.register(Group)
