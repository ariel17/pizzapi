#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration file for shop models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from order.models import Order, OrderState


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderStateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderState, OrderStateAdmin)
