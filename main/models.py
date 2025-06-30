from django.db import models
from djmoney.models.fields import MoneyField
from cities_light.models import City


class Position(models.Model):
    FORMATS = [
        ('remote', 'Удаленно'),
        ('onsite', 'Офис'),
        ('hybrid', 'Гибрид'),
        ('contract', 'Контракт'),
        ('flex', 'Гибкий'),
    ]
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    salary = models.MoneyField(max_digits=10, decimal_places=2,
                               default_currency="BYN", blank=True, null=True)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,
                             blank=True)
    format = models.CharField(max_length=10, choices=FORMATS,
                              default=FORMATS[0][0])
    date_of_request = models.DateField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.position} in {self.company}"

class StageOfInterview(models.Model):
    STATUS = [
        ('waiting', 'Ожидание'),
        ('accepted', 'Подтверждение'),
        ('rejected', 'Отказ'),
    ]
    title = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, default=STATUS[0][0])
    feedback = models.TextField()

    def __str__(self):
        return f"{title} - {self.position}"





