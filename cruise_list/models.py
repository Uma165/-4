from django.db import models


class Cruise(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    time = models.CharField(max_length=60, verbose_name='Время круиза')
    cities = models.CharField(max_length=128, verbose_name='Название городов')
    discription =models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=100, verbose_name='Цена')
    is_active = models.BooleanField(verbose_name='Активен', default=True, db_index=True)

    publish_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    edit_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата редактирования')

    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    view = models.CharField(max_length=128, verbose_name='Просмотры')

    class Meta:
        verbose_name = 'Маршруты и корабли'
        verbose_name_plural = 'Маршруты и корабли'
        ordering = ('-publish_date', '-edit_date')

    def __str__(self):
        return f'{self.title}; Города: {self.cities}'


class Room(models.Model):
    CATEGORIES = (
        ('inside', 'Внутренний'),
        ('oceanview', 'С окном'),
        ('balcony', 'С балконом'),
        ('suite', 'Люкс'),
    )

    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE, related_name='rooms')
    category = models.CharField(choices=CATEGORIES, max_length=10, default=None,
                                verbose_name='Категория')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    count = models.PositiveIntegerField(default=0, verbose_name='количество мест')

    class Meta:
        verbose_name = 'Категория кают'
        verbose_name_plural = 'Кактегории кают'
        ordering = ('cruise', 'category')

    def __str__(self):
        return f'{self.get_category_display()}, цена: {self.price}р.'
