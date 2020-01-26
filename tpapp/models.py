from django.conf import settings
from django.db import models


class AppData(models.Model):
    year = models.IntegerField(
        verbose_name='year'
    )

    month = models.IntegerField(
        verbose_name='month'
    )

    temperature = models.FloatField(
        verbose_name='temperature'
    )

    precipitation = models.FloatField(
        verbose_name='precipitation',
        null=True,
    )

    # Magic string method formats post string display
    def __str__(self):
        return f'ID: {self.id}  /  Year: {self.year}  /  Month: {self.month}  /  Temperature: {self.temperature}  /  Precipitation: {self.precipitation}'




