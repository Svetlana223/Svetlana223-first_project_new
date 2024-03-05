from django.contrib import admin
from .models import Product, User, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    readonly_fields = ['registration_date']
    fieldsets = [
        (

            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Личная информация',
            {
                'fields': ['email','phone_number', 'address'],
            }
        ),
        (
            'Дата регистрации',
            {
                'fields': ['registration_date'],
            }
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']
    readonly_fields = ['added_date']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Описание товара', 'fields': ['description', 'image'],
            },
        ),
        (
            'Цена и количество остатков',
            {
                'fields': ['price', 'stock'],
            }
        ),
        (
            'Дата добавления',
            {
                'fields': ['added_date'],
            }
        ),
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'order_date']



