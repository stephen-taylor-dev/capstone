from django.contrib import admin

# Register your models here.

from .models import User, Liturgy, Group, Group_Invite

# Register your models here.
admin.site.register(User)
admin.site.register(Liturgy)
admin.site.register(Group)
admin.site.register(Group_Invite)
