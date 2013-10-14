#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration file for client models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
