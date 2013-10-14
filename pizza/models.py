#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Pizza, providers and orders models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


class Ingredient(models.Model):
    """
    The pizza ingredients to apply.
    """

    name = models.CharField(_(u'Name'))

    def __unicode__(self):
        """
        The unicode instance representation for an ingredient.
        """
        return u'Ingredient: %s' % self.name


class Pizza(models.Model):
    """
    A pizza model about those to be delivered.
    """

    name = models.CharField(_(u'Name'))
    ingredients = models.ManyToMany(Ingredient)

    def __unicode__(self):
        """
        The unicode instance representation for a pizza.
        """
        return u'%s: Pizza with %s' % (self.name, ', '.join([i.name for i in
                                       self.ingredients]))
