from django.db import models

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        )
    title = models.CharField(
        max_length=128,
        blank=False,
        null=False,
    )
    subtitle = models.CharField(
        max_length=128,
        blank=True,
        default='',
        )
    content = models.TextField(
        blank=False,
        )
