# import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
from database import Database
database = Database()

base_url = "https://www.uniqlo.com"
base_page = "https://www.uniqlo.com/jp/store/feature/uq/sale/men/"
driver.implicitly_wait(50)
driver.get(base_page)
driver.find_elements(By.CLASS_NAME, 'unit')

html_source = driver.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(html_source, 'lxml')
driver.quit()

products = soup.findAll('div', {'class': 'unit'})
for product in products:
    category_id = 8 ## 1
    sub_category_id = 9 ## 2
    category_name = 'clothes' ## 3
    sub_category_name = 'uniqlo' ## 4
    name_ja = product.select_one(".name > a").getText() ## 5
    name_vi = name_ja ## 6
    brand = 'uniqlo'
    unit_price = product.select_one(".price").getText().replace('¥', '').replace(',', '').replace('\n', '').replace(' ', '') ## 7
    type = 'Uniqlo nam giảm giá' ## 8
    packing = 'origin' ## 9
    use_guide = None ## 10
    description = None ## 11
    age_gt = None ## 12
    age_lt = None ## 13
    sex = 'male' ## 14
    color = product.select('.l3_alias_color_chip > img')
    for i in range(len(color)):
        color[i] = 'https:' + color[i].attrs['color_chip_image']
    color = ','.join(color) ## 15
    image = product.select_one(".thumb > a > img").attrs['color_chip_image'] ## 16
    origin_product_code = 'uniqlo-' + product.select_one(".l3_alias_color_chip").attrs['data-item-code'] ## 17
    url = product.select_one(".info > .name > a").attrs['href'].replace(base_url, '')
    origin_url = base_url + url ## 18
    active_status = 1 ## 19
    stock_status = 1 ## 20
    sale_status = 1 ## 21
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S") ## 22
    data_base = (category_id, sub_category_id, category_name, sub_category_name, name_vi, name_ja, brand, unit_price, type, packing, use_guide, description, age_gt, age_lt, sex, color, image, origin_product_code, origin_url, active_status, stock_status, sale_status, created)

    # print(data_base)
    # print('-------------------------------------------------------------')
    database.insertProduct(data_base)
    # exit()

exit()