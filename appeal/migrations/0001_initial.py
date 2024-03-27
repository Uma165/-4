# Generated by Django 5.0 on 2024-03-27 17:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Вечерний путь', 'Вечерний путь'), ('Моряк', 'Моряк'), ('Рай над морем', 'Рай над морем'), ('Воздушный корабль', 'Воздушный корабль')], max_length=128, verbose_name='Круиз')),
                ('сapacity', models.CharField(max_length=60, verbose_name='Количество человек')),
                ('datecruise', models.DateField(verbose_name='Дата отправки')),
                ('contact', models.CharField(max_length=128, verbose_name='Контактая информация')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('status', models.CharField(choices=[('a', 'В обработке'), ('b', 'Выполнено'), ('c', 'Отклонено')], max_length=100, verbose_name='Статус')),
                ('uid', models.CharField(db_index=True, max_length=64, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='answer/%Y/%m/%d')),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
                ('appeal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='appeal.appeal', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ('-send_date', '-update_date'),
            },
        ),
    ]
