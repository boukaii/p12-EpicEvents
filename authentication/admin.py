# from django.contrib import admin
# from authentication.models import User
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#
#     list_display = ("last_name", "first_name", "team")
#     fields = (("first_name", "last_name"), "email", "role", "password", "is_active")
from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("last_name", "first_name", "team")
    list_filter = ("team", )
    fields = (("first_name", "last_name"), "email", "team", "is_active")


admin.site.register(User, UserAdmin)
