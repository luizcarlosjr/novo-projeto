from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    Autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=200)
    Texto = models.TextField()
    Data_Criacao = models.DateTimeField(default=timezone.now)
    Data_Publicao = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title