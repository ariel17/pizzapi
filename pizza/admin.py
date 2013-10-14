#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration file for pizza models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from pizza.models import Ingredient, Pizza


class IngredientAdmin(admin.ModelAdmin):
    pass


class PizzaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Pizza, PizzaAdmin)
