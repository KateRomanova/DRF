from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import datetime
from django.utils.timezone import now

from materials.models import Course, Lesson

payment_choices = (
    ("Наличные", "Наличные"),
    ("Перевод на счет", "Перевод на счет"),
)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="электронная почта", help_text="укажите эл. почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        blank=True,
        null=True,
        help_text="укажите телефон",
    )
    city = models.CharField(
        max_length=35,
        verbose_name="город",
        blank=True,
        null=True,
        help_text="укажите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="аватар",
        help_text="загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Payments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="пользователь",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    payment_date = models.DateTimeField(default=now, verbose_name='Дата оплаты', blank=True, null=True)
    course = models.ForeignKey(Course, verbose_name='Оплаченный курс', on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, verbose_name='Оплаченный урок', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')
    payment_type = models.CharField(max_length=50, verbose_name='Способ оплаты', default='Перевод на счет',
                                    choices=payment_choices)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
