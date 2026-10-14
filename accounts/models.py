from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin',
        PATIENT = 'PATIENT', 'Bemor',
        DOCTOR = 'DOCTOR', 'Shifokor',
        DRIVER = 'DRIVER', 'Haydovchi',

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT,
        help_text="Роль пользователя в системе"
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        help_text="Telefon Nomer(masalan:+9980000000)"
    )
    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        return f"{self.username} | {self.get_role_display()}"


