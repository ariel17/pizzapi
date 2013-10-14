#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration file for shop models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from shop.models import Shop, Order, OrderState, Delivery, DeliveryState


class ShopAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderStateAdmin(admin.ModelAdmin):
    pass


class DeliveryAdmin(admin.ModelAdmin):
    pass


class DeliveryStateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shop, ShopAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderState, OrderStateAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryState, DeliveryStateAdmin)
