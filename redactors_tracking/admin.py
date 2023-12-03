from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from redactors_tracking.models import Redactor, Newspaper, Topic


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("license",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "license",
                    )
                },
            ),
        )
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("topic",)


admin.site.register(Topic)
