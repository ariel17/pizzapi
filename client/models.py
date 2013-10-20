#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Client information; by now, just that.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from common.models import Address, Phone


class Client(models.Model):
    """
    The client identification model.
    """
    user = models.OneToOneField(User)
    address = models.ManyToManyField('ClientAddress', related_name='+')
    phone = models.ManyToManyField('ClientPhone', related_name='+')


class ClientAddress(Address):
    """
    The client address model.
    """
    client = models.ForeignKey('Client')


class ClientPhone(Phone):
    """
    TODO
    """
    client = models.ForeignKey('Client')
