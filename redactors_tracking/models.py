from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Topic(models.Model):
    name = models.CharField(max_length=55, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField(null=True, blank=True)
    published_data = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="newspapers")
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="publishers")

    class Meta:
        ordering = ["-published_data"]

    def __str__(self) -> str:
        return f"{self.title} {self.topic.name}"


class Redactor(AbstractUser):
    redactor_id = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name}, {self.last_name})"
