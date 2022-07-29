# Generated by Django 3.2.5 on 2022-07-29 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benedict_option', '0006_alter_user_current_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='current_groups',
        ),
        migrations.AddField(
            model_name='user',
            name='active_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_group', to='benedict_option.group'),
        ),
    ]