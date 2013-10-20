#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Administration file for client models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from client.models import Client, ClientAddress, ClientPhone


class ClientAddressInline(admin.TabularInline):
    """
    TODO
    """
    model = ClientAddress


class ClientPhoneInline(admin.TabularInline):
    """
    TODO
    """
    model = ClientPhone


class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, { 'fields': ('user', ) }
        ),
    )
    inlines = (ClientAddressInline, ClientPhoneInline)


admin.site.register(Client, ClientAdmin)
