# import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from database import Database
database = Database()

sub_category_name = 'uniqlo'

products = database.selectProductBySubCategory(sub_category_name)
for product in products:
    # print(product)
    product_url = product['origin_url']
    origin_url_split = product_url.split('-')
    origin_url = origin_url_split[0]
    # print(origin_url)
    origin_code = origin_url.replace('https://www.uniqlo.com/jp/store/goods/', '')
    # print(origin_code)
    # exit()
    # driver.implicitly_wait(10)
    driver = webdriver.Firefox()
    driver.get(origin_url)
    driver.find_elements(By.CLASS_NAME, 'unit')
    html_source = driver.execute_script('return document.documentElement.outerHTML')
    soup_base = BeautifulSoup(html_source, 'lxml')
    driver.quit()
    stock_status = soup_base.find('div', {'id': 'msgProdStockOut'})
    images = soup_base.select('#prodThumbImgs > li')
    prod_colors = soup_base.select('#listChipColor > li > .chipCover')
    # print(prod_colors)
    # exit()
    for i in range(len(images)):
        images[i] = '<img src="https://im.uniqlo.com/images/jp/pc/goods/' + origin_code + '/sub/' + images[i].attrs['code'] + '_popup.jpg">'
    images = '</br></br>'.join(images)

    for q in range(len(prod_colors)):
        prod_colors[q] = '<img src="https://im.uniqlo.com/images/jp/pc/goods/' + origin_code + '/item/' + prod_colors[q].attrs['color'] + '_' +  origin_code + '.jpg">'
    prod_colors = '</br></br>'.join(prod_colors)

    all_images = images + prod_colors
    # exit()

    database.updateImage(all_images, product['id'])

    # if stock_status != None:
        # print('out of stock')
        # exit()
        # database.updateUniqloStatus(product['id'])
