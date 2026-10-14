from django.db import models
from django.conf import settings

# Create your models here.


class Hospital(models.Model):
    """
    Shifoxonalar modeli: joylashuvi, bo'sh o'rinlari va aloqa ma'lumotlari.
    """
    name = models.CharField(max_length=255, verbose_name="Shifoxona nomi")
    address = models.TextField(verbose_name="Manzili")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Kenglik (Latitude)"
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Uzunlik (Longitude)"
    )
    total_beds = models.IntegerField(default=0, verbose_name="Umumiy o'rinlar soni")
    available_beds = models.IntegerField(default=0, verbose_name="Bo'sh o'rinlar soni")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Shifoxona"
        verbose_name_plural = "Shifoxonalar"

    def __str__(self) -> str:
        return f"{self.name} (Bo'sh o'rinlar: {self.available_beds})"


class Ambulance(models.Model):
    """
    Tez yordam mashinalari va ularning holati modeli.
    """
    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Bo\'sh'
        BUSY = 'BUSY', 'Chaqiruvda'
        MAINTENANCE = 'MAINTENANCE', 'Ta\'mirda'

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='ambulances',
        verbose_name="Biriktirilgan shifoxona"
    )
    driver = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'DRIVER'},
        related_name='ambulance',
        verbose_name="Haydovchi"
    )
    license_plate = models.CharField(max_length=20, unique=True, verbose_name="Davlat raqami")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
        verbose_name="Holati"
    )
    current_latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Hozirgi kenglik"
    )
    current_longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Hozirgi uzunlik"
    )

    class Meta:
        verbose_name = "Tez yordam mashinasi"
        verbose_name_plural = "Tez yordam mashinalari"

    def __str__(self) -> str:
        return f"Tez yordam {self.license_plate} - {self.get_status_display()}"


class EmergencyCall(models.Model):
    """
    Bemorlar tomonidan qilingan shoshilinch chaqiruvlar modeli.
    """
    class Priority(models.TextChoices):
        LOW = 'LOW', 'Past'
        MEDIUM = 'MEDIUM', 'O\'rta'
        HIGH = 'HIGH', 'Yuqori (Shoshilinch)'

    class CallStatus(models.TextChoices):
        PENDING = 'PENDING', 'Kutilmoqda'
        DISPATCHED = 'DISPATCHED', 'Yo\'lda'
        ARRIVED = 'ARRIVED', 'Yetib bordi'
        COMPLETED = 'COMPLETED', 'Bajarildi'

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='emergency_calls',
        limit_choices_to={'role': 'PATIENT'},
        verbose_name="Bemor"
    )
    ambulance = models.ForeignKey(
        Ambulance,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_calls',
        verbose_name="Biriktirilgan tez yordam"
    )
    pickup_latitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Chaqiruv kengligi"
    )
    pickup_longitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name="Chaqiruv uzunligi"
    )
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
        verbose_name="Muhimlik darajasi"
    )
    status = models.CharField(
        max_length=20,
        choices=CallStatus.choices,
        default=CallStatus.PENDING,
        verbose_name="Chaqiruv holati"
    )
    symptoms_description = models.TextField(verbose_name="Simptomlar tavsifi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Shoshilinch chaqiruv"
        verbose_name_plural = "Shoshilinch chaqiruvlar"

    def __str__(self) -> str:
        return f"Chaqiruv #{self.id} - {self.get_priority_display()} ({self.get_status_display()})"