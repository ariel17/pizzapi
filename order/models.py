#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Order details and status.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


class Order(models.Model):
    """
    What the client wants as a pizza.
    """

    client = models.ForeignKey('client.Client')
    promotion = models.ManyToManyField('shop.Promotion')
    shop = models.ForeignKey('shop.Shop', null=True)


class OrderState(models.Model):
    """
    The order state.
    """

    PENDING = 'pe'
    COOKING = 'co'
    DELIVERED = 'de'
    CANCELLED = 'ca'

    STATE_CHOICES = (
        (PENDING, _('Pending')),
        (COOKING, _('Cooking')),
        (DELIVERED, _('Delivered')),
        (CANCELLED, _('Cancelled')),
    )

    order = models.ForeignKey('Order')
    state = models.CharField(max_length=2, choices=STATE_CHOICES,
                             default=PENDING)
