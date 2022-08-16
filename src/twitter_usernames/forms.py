from django import forms
from . import models


class UsernameForm(forms.ModelForm):
    class Meta:
        model = models.Username
        fields = ("username",)
