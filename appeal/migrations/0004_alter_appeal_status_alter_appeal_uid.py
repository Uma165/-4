# Generated by Django 5.0.4 on 2024-04-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0003_remove_type_add_fks_to_cruise_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='status',
            field=models.CharField(choices=[('a', 'В обработке'), ('b', 'Выполнено'), ('c', 'Отклонено')], default='a', max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='uid',
            field=models.CharField(blank=True, db_index=True, max_length=64, unique=True),
        ),
    ]