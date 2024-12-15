from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_ROLES = [
        ('leader', 'Глава'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
        ('user', 'Пользователь'),
       ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='user')

    def __str__(self):
           return self.user.username