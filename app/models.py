from django.db import models
from django.utils import timezone
# Create your models here.

class Search(models.Model):
    text = models.CharField(max_length=500)
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Searches"

    def __str__(self):
        return self.text
    