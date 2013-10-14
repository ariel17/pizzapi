#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Pizza shop models!
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from common.models import Address
from pizza.models import Pizza


class Shop(Address):
    """
    The pizza shop and menu.
    """

    user = models.OneToOneField(User)
    pizzas = models.ManyToManyField(Pizza)


class Order(models.Model):
    """
    What the client wants as a pizza.
    """

    client = models.ForeignKey('client.Client')
    pizzas = models.ManyToManyField('pizza.Pizza')
    shop = models.ForeignKey('Shop', null=True)


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


class Delivery(models.Model):
    """
    What the client wants as a pizza, how much it costs.
    """

    order = models.ForeignKey('Order')
    shop = models.ForeignKey('Shop')
    charge = models.DecimalField(max_digits=3, decimal_places=2)


class DeliveryState(models.Model):
    """
    The delivery state.
    """

    PENDING = 'pe'
    ON_ITS_WAY = 'on'
    COMPLETED = 'co'

    STATE_CHOICES = (
        (PENDING, _(u'Pending')),
        (ON_ITS_WAY, _(u'On its way')),
        (COMPLETED, _(u'Completed')),
    )

    delivery = models.ForeignKey('Delivery')
    state = models.CharField(max_length=2, choices=STATE_CHOICES,
                             default=PENDING)
