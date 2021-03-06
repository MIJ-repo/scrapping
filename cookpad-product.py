import requests
import re
import json
from datetime import datetime
from bs4 import BeautifulSoup
from cookpad_db import Database
database = Database()

def getProductUrl(url, page_no):
    page_html = requests.get(url + '?page=' + str(page_no))
    soup = BeautifulSoup(page_html.text, 'html.parser')
    return soup.find_all('a', {'class': 'recipe-title'})

def getProductContent(url):
    page_html = requests.get(url)
    soup = BeautifulSoup(page_html.text, 'html.parser')
    print(soup)

def getTotalPageNumber(url):
    page_html = requests.get(url)
    soup = BeautifulSoup(page_html.text, 'html.parser')
    return int(soup.select_one('.page_num').getText().replace('1 / ', '').replace('ページ', '').replace('\n', '').replace(',', ''))

base_url = 'https://cookpad.com'
product_base_url = 'https://cookpad.com/recipe/'
parents_category = database.getParentsCategory()
count = 41839
for parents in parents_category:
    children_category = database.getChildrenCategoryByParentId(parents.get('id'))
    for children in children_category:
        grandchildren_category = database.getChildrenCategoryByParentId(children.get('id'))
        for grandchildren in grandchildren_category:
            great_grandchildrens = database.getChildrenCategoryByParentIdExcept(grandchildren.get('id'))
            for great_grandchildren in great_grandchildrens:
                for page_no in range(1, getTotalPageNumber(great_grandchildren.get('origin_url'))):
                    products_url = getProductUrl(great_grandchildren.get('origin_url'), page_no)
                    for product_url in products_url:
                        if base_url not in product_url.attrs['href']:
                            product_url = base_url + product_url.attrs['href']
                        else:
                            product_url = product_url.attrs['href']
                        category_id = great_grandchildren.get('id')
                        code = 'R' + product_url.replace(product_base_url, '')
                        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        data = (category_id, code, product_url, created)
                        database.insertProductOriginUrl(data)
                        print(count)
                        count += 1
                        