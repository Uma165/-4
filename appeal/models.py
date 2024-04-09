import hashlib
from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
from cruise_list.models import Cruise, Room


class Appeal(models.Model):
    # TYPES = (
    #     ('Вечерний путь', 'Вечерний путь'),
    #     ('Моряк', 'Моряк'),
    #     ('Рай над морем', 'Рай над морем'),
    #     ('Воздушный корабль', 'Воздушный корабль'),
    # )
    # type = models.CharField(choices=TYPES, max_length=128, verbose_name='Круиз')

    STATUS_CHOICE = (("a", "В обработке"),
                     ("b", "Выполнено"),
                     ("c", "Отклонено"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appeals',
        null=True, default=None, verbose_name='Пользователь')
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, related_name='appeals',
        null=True, default=None, verbose_name='Круиз')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='appeals',
        null=True, default=None, verbose_name='Комната')
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICE, default='a')

    capacity = models.CharField(max_length=60, verbose_name='Количество человек')
    contact = models.CharField(max_length=128, verbose_name='Контактая информация')
    email = models.EmailField("Электронная почта", blank=False)
    uid = models.CharField(max_length=64, blank=True, null=False, db_index=True, unique=True)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def generate_uid(self):
        while True:
            uid = ( str(self.contact) + str(self.cruise.title)
                   + str(self.capacity) + str(datetime.now().timestamp()) )
            m = hashlib.sha256()
            m.update(bytes(uid, encoding='utf-8'))
            uid = m.hexdigest()

            if len(Appeal.objects.filter(uid=uid)) == 0:
                break
        return uid

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = self.generate_uid()

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'От пользователя: {self.contact} на круиз: {self.cruise_id}'


class Answer(models.Model):
    text = models.TextField(blank=False)
    file = models.FileField(upload_to='answer/%Y/%m/%d', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль')
    send_date = models.DateTimeField('Дата отправки', auto_now_add=True)
    update_date = models.DateTimeField('Дата редактирования', auto_now=True)
    appeal = models.OneToOneField(Appeal, on_delete=models.CASCADE, related_name='answer', verbose_name='Заявка')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('-send_date', '-update_date')

    def __str__(self):
        date = self.send_date.strftime('%d.%m.%Y %H:%m')
        return f'{date}. Ответ: {self.text[0:30]}...'
