#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Client information; by now, just that.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _

from common.models import Address
from pizza.models import Pizza


class Client(Address):
    """
    """
    pass
