# Generated by Django 5.0.4 on 2024-04-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_email_token_profile_preferred_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_token',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
