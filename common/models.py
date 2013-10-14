#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Common models to share between applications.
Source: http://djangosnippets.org/snippets/1177/
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    """
    Model containing the all related information about address location.
    """

    TYPES_CHOICES = (
        (u'HOME', _(u'Home')),
        (u'WORK', _(u'Work')),
        (u'OTHER', _(u'Other'))
    )

    type = models.CharField(_(u'Type'), maxlength=20, choices=TYPES_CHOICES)
    street_line1 = models.CharField(_(u'Address 1'), max_length=100,
                                    blank=True)
    street_line2 = models.CharField(_(u'Address 2'), max_length=100,
                                    blank=True)
    building = models.CharField(_(u'Building'), max_length=20, blank=True)
    departement = models.CharField(_(u'Departement'), max_length=50,
                                   blank=True)
    floor = models.CharField(_(u'Floor'), max_length=20, blank=True)
    door = models.CharField(_(u'Door'), max_length=20, blank=True)
    number = models.CharField(_(u'Number'), max_length=30, blank=True)
    zipcode = models.CharField(_(u'ZIP code'), max_length=5, blank=True)
    city = models.CharField(_(u'City'), max_length=100, blank=True)
    state = models.CharField(_(u'State'), max_length=100, blank=True)
    postal_box = models.CharField(_('Postal box'), max_length=20, blank=True)
    country = models.CharField(_('Country'), max_length=100, blank=True)
