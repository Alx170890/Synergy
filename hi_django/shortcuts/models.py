from django.db import models
from django.contrib.auth.models import User

class ShortUrl(models.Model):
    key = models.CharField(max_length=256)
    url = models.URLField()
    short = models.URLField()
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.url} - {self.short} -{self.key} - {self.visits}'