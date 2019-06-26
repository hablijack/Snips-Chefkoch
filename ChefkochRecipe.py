#!/usr/bin/python3
# -*- coding: utf-8 -*-

class ChefkochRecipe(object):
    def __init__(self, name="", description="", image="", ingredients=[]):
        self.name = name
        self.description = description
        self.image = image
        self.ingredients = ingredients
