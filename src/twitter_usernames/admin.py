from django.contrib import admin
from . import models


class UsernameAdmin(admin.ModelAdmin):
    list_display = [
        "username",
    ]


admin.site.register(models.Username, UsernameAdmin)
