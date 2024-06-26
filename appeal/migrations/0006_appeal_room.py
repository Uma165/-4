# Generated by Django 5.0.4 on 2024-04-08 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0005_alter_appeal_cruise_alter_appeal_user'),
        ('cruise_list', '0007_alter_room_cruise'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='room',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appeals', to='cruise_list.room', verbose_name='Комната'),
        ),
    ]
