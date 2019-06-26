#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import feedparser
from ChefkochRecipe import ChefkochRecipe

class Chefkoch:

    def __init__(self, config):
        pass

    def recipe_of_the_day(self):
        recipe = self.fetch()
        return "Wie wäre es mit: {0}?".format(recipe.name)

    def fetch(self):
        chefkoch_recipe_url = "https://www.chefkoch.de/rezepte/"
        chefkoch_recipe_of_the_day_rss_url = "https://www.chefkoch.de/rss/rezept-des-tages.php"
        feed = feedparser.parse(chefkoch_recipe_of_the_day_rss_url)
        url = feed['entries'][0]['link']
        url = url.replace(chefkoch_recipe_url, "")
        recipe_id =  url.split("/")[0]
        recipe = ChefkochRecipe()
        url = chefkoch_recipe_url + str(recipe_id)
        req = requests.get(url)
        contents = BeautifulSoup(req.text, 'lxml')
        recipe.name = contents.find('h1', class_='page-title').text
        ingredients_table = contents.find('table', class_='incredients')
        recipe.description = contents.find('div', id='rezept-zubereitung').text.strip()
        recipe.image = contents.find('img', class_='slideshow-image')['src']

        for row in ingredients_table.findAll('tr'):
            col = row.findAll('td')
            ingredient = "{} {}".format(col[0].text.strip(), col[1].text.strip())
            ingredient = ingredient.replace("\xa0", "")
            recipe.ingredients.append(ingredient)
        return recipe
