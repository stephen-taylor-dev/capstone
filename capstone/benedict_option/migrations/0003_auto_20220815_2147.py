# Generated by Django 3.2.5 on 2022-08-15 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('benedict_option', '0002_group_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_invite',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group_invite',
            name='user',
            field=models.ForeignKey(default=1625309472.357246, on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='benedict_option.user'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='group_invite',
            name='receiver',
        ),
        migrations.AddField(
            model_name='group_invite',
            name='receiver',
            field=models.ManyToManyField(related_name='receivers', to=settings.AUTH_USER_MODEL),
        ),
    ]