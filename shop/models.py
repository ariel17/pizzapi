#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Pizza shop models!
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from common.models import Address, Phone


class Shop(Address):
    """
    The pizza shop and menu.
    """

    user = models.OneToOneField(User)
    address = models.ManyToManyField('ShopAddress')
    phone = models.ManyToManyField('ShopPhone')


class ShopAddress(Address):
    """
    The shop address model.
    """
    pass


class ShopPhone(Phone):
    """
    TODO
    """
    pass


class Promotion(models.Model):
    """
    A shop promotion for pizzas or combos.
    """

    shop = models.ForeignKey('Shop')
    pizza = models.ForeignKey('pizza.Pizza')
    charge = models.DecimalField(max_digits=3, decimal_places=2)


class Delivery(models.Model):
    """
    What the client wants as a pizza, how much it costs.
    """

    order = models.ForeignKey('order.Order')
    shop = models.ForeignKey('Shop')


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
