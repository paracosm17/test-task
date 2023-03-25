from django.contrib import admin

from .models import CustomUser, Car


class CarAdminInline(admin.TabularInline):
    model = Car


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    inlines = (CarAdminInline, )


class CarAdmin(admin.ModelAdmin):
    model = Car


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Car, CarAdmin)
