import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from database import Database
database = Database()

base_url = "https://www.matsukiyo.co.jp"
base_page = "https://www.matsukiyo.co.jp/store/online/search?category=00331962"
more_product_url = "https://www.matsukiyo.co.jp/store/api/search/next?query=po%255B%255D%3D%25E5%258C%2596%25E7%25B2%25A7%25E5%2593%2581%3A%25E8%25B3%2587%25E7%2594%259F%25E5%25A0%2582%25E3%2582%25AB%25E3%2582%25A6%25E3%2583%25B3%25E3%2582%25BB%25E3%2583%25AA%25E3%2583%25B3%25E3%2582%25B0%3A%25EF%25BC%25A4%25E3%2583%2597%25E3%2583%25AD%25E3%2582%25B0%25E3%2583%25A9%25E3%2583%25A0%3A%25E5%258C%2596%25E7%25B2%25A7%25E6%25B0%25B4%26limit%3D12%26sort%3DScore%2Crank%2Cnumber5%2CNumber19%26fmt%3Djson&backurl=undefined"

base_page_html = requests.get(base_page)
more_product_html = requests.get(more_product_url)

soup_base = BeautifulSoup(base_page_html.text, 'html.parser')
ul_product_base = soup_base.find('ul', {'id': 'itemList'})
product_base = ul_product_base.findChildren('li', recursive=False)
for product in product_base:
    category_id = 1
    sub_category_id = 2
    category_name = 'cosmetics'
    sub_category_name = 'shiseido'
    name_vi = product.select_one(".ttl > a").getText()
    name_ja = product.select_one(".ttl > a").getText()
    unit_price = product.select_one(".price").getText().replace('円(税込)', '').replace(',', '')
    type = 'Elixir Advanced'
    packing = 'Box'
    use_guide = 'Chua co'
    description = product.select_one(".rightBox").getText()
    image = base_url + product.select_one(".img > a > img").attrs['src']
    origin_product_code = product.select_one('.button.cart').attrs['data-code']
    origin_url = base_url + product.select_one('.ttl > a').attrs['href']
    active_status = 1
    stock_status = 1
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_base = (category_id, sub_category_id, category_name, sub_category_name, name_vi, name_ja, unit_price, type, packing, use_guide, description, image, origin_product_code, origin_url, active_status, stock_status, created)
    print(data_base)
    database.insertProduct(data_base)
    print("*****************************************************************************************")

# # ==========================================================================
soup_more = BeautifulSoup(more_product_html.json()['list'], 'html.parser')
product_more = soup_more.findChildren('li', recursive=False)
for product in product_more:
    category_id = 1
    sub_category_id = 2
    category_name = 'cosmetics'
    sub_category_name = 'shiseido'
    name_vi = product.select_one(".ttl > a").getText()
    name_ja = product.select_one(".ttl > a").getText()
    unit_price = product.select_one(".price").getText().replace('円(税込)', '').replace(',', '')
    type = 'Elixir Advanced'
    packing = 'Box'
    use_guide = 'Chua co'
    description = product.select_one(".rightBox").getText()
    image = base_url + product.select_one(".img > a > img").attrs['src']
    origin_product_code = product.select_one('.button.cart').attrs['data-code']
    origin_url = base_url + product.select_one('.ttl > a').attrs['href']
    active_status = 1
    stock_status = 1
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_more = (category_id, sub_category_id, category_name, sub_category_name, name_vi, name_ja, unit_price, type, packing, use_guide, description, image, origin_product_code, origin_url, active_status, stock_status, created)
    # print(data_more)
    # database.insertProduct(data_more)
    # print("*****************************************************************************************")
