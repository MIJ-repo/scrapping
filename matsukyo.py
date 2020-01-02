import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from database import Database
database = Database()

base_url = "https://www.matsukiyo.co.jp"
base_page = "https://www.matsukiyo.co.jp/store/online/search?category=0012021306"
more_product_url = "https://www.matsukiyo.co.jp/store/api/search/next?query=po%255B%255D%3D%25E5%258C%25BB%25E8%2596%25AC%25E5%2593%2581%25E3%2583%25BB%25E5%258C%25BB%25E8%2596%25AC%25E9%2583%25A8%25E5%25A4%2596%25E5%2593%2581%3A%25E4%25B8%2580%25E8%2588%25AC%25E5%2581%25A5%25E5%25BA%25B7%25E9%25A3%259F%25E5%2593%2581%25EF%25BC%2588%25E7%25BE%258E%25E5%25AE%25B9%25E3%2583%25BB%25E7%2594%259F%25E6%25B4%25BB%25E7%25BF%2592%25E6%2585%25A3%25EF%25BC%2589%3A%25E7%2594%259F%25E6%25B4%25BB%25E6%2594%25B9%25E5%2596%2584%3A%25E8%25A1%2580%25E6%25B5%2581%25E6%2594%25B9%25E5%2596%2584%26limit%3D16%26sort%3DScore%2Cnumber5%2Crank%2CNumber19%26fmt%3Djson&backurl=undefined"

base_page_html = requests.get(base_page)
more_product_html = requests.get(more_product_url)

soup_base = BeautifulSoup(base_page_html.text, 'html.parser')
ul_product_base = soup_base.find('ul', {'id': 'itemList'})
product_base = ul_product_base.findChildren('li', recursive=False)
for product in product_base:
    category_id = 1 #1
    sub_category_id = 74 #2
    category_name = 'pharmacy' #3
    sub_category_name = 'health_food' #4
    name_vi = product.select_one(".ttl > a").getText() #5
    name_ja = product.select_one(".ttl > a").getText() #6
    brand = None #7
    unit_price_get = product.select_one(".price").getText().replace('\n本体\r\n\t\t\t\t', '').replace('円', '').replace(',', '') #8
    unit_price = round(float(unit_price_get)*1.1)
    type = 'Thải ure' #9
    packing = 'Box' #10
    use_guide = None #11
    description = product.select_one(".rightBox").getText() #12
    age_gt = None ## 13
    age_lt = None ## 14
    sex = None ## 15
    color = None ##16
    image = base_url + product.select_one(".img > a > img").attrs['src'] ##17
    origin_product_code = product.select_one('.button.cart').attrs['data-code'] ##18
    origin_url = base_url + product.select_one('.ttl > a').attrs['href'] ##19
    active_status = 1 ##20
    stock_status = 1 ##21
    sale_status = 1 ##22
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S") ##23
    data_base = (category_id, sub_category_id, category_name, sub_category_name, name_vi, name_ja, brand, unit_price, type, packing, use_guide, description, age_gt, age_lt, sex, color, image, origin_product_code, origin_url, active_status, stock_status, sale_status, created)
    print(data_base)
    database.insertProduct(data_base)
    print("*****************************************************************************************")

# # ==========================================================================
soup_more = BeautifulSoup(more_product_html.json()['list'], 'html.parser')
product_more = soup_more.findChildren('li', recursive=False)
for product in product_more:
    category_id = 1 #1
    sub_category_id = 74 #2
    category_name = 'pharmacy' #3
    sub_category_name = 'health_food' #4
    name_vi = product.select_one(".ttl > a").getText() #5
    name_ja = product.select_one(".ttl > a").getText() #6
    brand = None #7
    unit_price_get = product.select_one(".price").getText().replace('\n本体\r\n\t\t\t\t', '').replace('円', '').replace(',', '') #8
    unit_price = round(float(unit_price_get)*1.1)
    type = 'Thải ure' #9
    packing = 'Box' #10
    use_guide = None #11
    description = product.select_one(".rightBox").getText() #12
    age_gt = None ## 13
    age_lt = None ## 14
    sex = None ## 15
    color = None ##16
    image = base_url + product.select_one(".img > a > img").attrs['src'] ##17
    origin_product_code = product.select_one('.button.cart').attrs['data-code'] ##18
    origin_url = base_url + product.select_one('.ttl > a').attrs['href'] ##19
    active_status = 1 ##20
    stock_status = 1 ##21
    sale_status = 1 ##22
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S") ##23
    data_more = (category_id, sub_category_id, category_name, sub_category_name, name_vi, name_ja, brand, unit_price, type, packing, use_guide, description, age_gt, age_lt, sex, color, image, origin_product_code, origin_url, active_status, stock_status, sale_status, created)
    # print(data_more)
    # database.insertProduct(data_more)
    # print("*****************************************************************************************")
