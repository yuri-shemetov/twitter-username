from django.db import models
from django.urls import reverse


class Username(models.Model):
    username = models.TextField(
        verbose_name="Username from twitter",
    )

    followers = models.IntegerField(
        verbose_name="followers",
        blank=True,
        null=True,
    )

    following = models.IntegerField(
        verbose_name="following",
        blank=True,
        null=True,
    )

    description = models.CharField(
        max_length=256,
        verbose_name="description",
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        verbose_name="Created",
        auto_now=False,
        auto_now_add=True,
    )

    def get_absolute_url(self):
        return reverse("usernames")

    class Meta:
        verbose_name = "Username"
        verbose_name_plural = "Usernames"
