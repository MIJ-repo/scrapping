import requests
import re
import json
from datetime import datetime
from bs4 import BeautifulSoup
from cookpad_db import Database
database = Database()

def getProductContent(url):
    page_html = requests.get(url)
    soup = BeautifulSoup(page_html.text, 'html.parser')
    return soup

def getProductName(page_content):
    return page_content.select_one('.recipe-title').getText().replace('"', '')

def getProductImage(page_content):
    if page_content.select_one('#main-photo > img').has_attr('data-large-photo'):
        return page_content.select_one('#main-photo > img').attrs['data-large-photo']
    else:
        return None

def getProductDescription(page_content):
    return page_content.select_one('.description_text').getText()

def getPeopleQuantity(page_content):
    if page_content.select_one('.servings_for'):
        return page_content.select_one('.servings_for').getText().replace('（', '').replace('）', '').replace(' ', '')
    else:
        return None
        

def getProductMaterial(page_content):
    return page_content.find_all('div', {'class': 'ingredient_row'})

def getProductStep(page_content):
    return page_content.find_all('div', {'class': 'step'})

def getMemo(page_content):
    return page_content.select_one('#history').getText()

products = database.selectProduct()
for product in products:
    count = 1
    page_content = getProductContent(product.get('origin_url'))
    name = getProductName(page_content)
    description = getProductDescription(page_content)
    image = getProductImage(page_content)
    memo = getMemo(page_content)
    people_quantity = getPeopleQuantity(page_content)
    database.updateProduct(name, description, image, memo, people_quantity, product.get('id'))
    for material in getProductMaterial(page_content):
        if material.select_one('.ingredient_name > .name'):
            name = material.select_one('.ingredient_name > .name').getText()
            quantity = material.select_one('.ingredient_quantity').getText()
            data = (product.get('id'), name, quantity, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            database.insertMaterial(data)
    for step in getProductStep(page_content):
        image = step.select_one('img').attrs['data-large-photo'] if step.select_one('img') else None
        ordinal = count
        content = step.select_one('.step_text').getText().replace('\n', '')
        data = (product.get('id'), ordinal, content, image, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        database.insertStep(data)