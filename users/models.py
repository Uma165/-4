from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    ROOM_CATEGORIES = (
        ('inside', 'Внутренний'),
        ('oceanview', 'С окном'),
        ('balcony', 'С балконом'),
        ('suite', 'Люкс'),
    )
    preferred_room_category = models.CharField(choices=ROOM_CATEGORIES, max_length=10,
        verbose_name='Предпочитаемая категория кают', null=True, default=None, blank=True)
    preferred_room_price_min = models.PositiveIntegerField(default=None, null=True, blank=True,
        verbose_name='Предпочитаемая цена от')
    preferred_room_price_max = models.PositiveIntegerField(default=None, null=True, blank=True,
        verbose_name='Предпочитаемая цена до')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email_token = models.CharField(max_length=128, null=True, default=None, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def is_email_confirmed(self):
        return self.email_token is None

    @classmethod
    def confirm_email_by_token(cls, token):
        if not token:
            return None
        profile = Profile.objects.get(email_token=token)
        profile.email_token = None
        profile.save()
        return profile

    def __str__(self):
        return f'{self.user.username} ({self.user.get_full_name()})'
