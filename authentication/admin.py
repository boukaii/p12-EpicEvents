from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("last_name", "first_name", "team")
    list_filter = ("team", )
    fields = (("first_name", "last_name"), "email", "team", "is_active")


admin.site.register(User, UserAdmin)
