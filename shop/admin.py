#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration file for shop models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from shop.models import Shop, ShopAddress, ShopPhone, Delivery, \
    DeliveryState, Promotion


class ShopAddressAdmin(admin.ModelAdmin):
    pass


class ShopPhoneAdmin(admin.ModelAdmin):
    pass


class ShopAdmin(admin.ModelAdmin):
    pass


class PromotionAdmin(admin.ModelAdmin):
    pass


class DeliveryAdmin(admin.ModelAdmin):
    pass


class DeliveryStateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopAddress, ShopAddressAdmin)
admin.site.register(ShopPhone, ShopPhoneAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryState, DeliveryStateAdmin)
