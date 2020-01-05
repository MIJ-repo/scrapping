# import requests
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
from database import Database
database = Database()

base_url = "https://www.abc-mart.net"
# base_page = "https://www.abc-mart.net/shop/r/r0542_p1_x1/#goodslist"

# base_page_html = requests.get(base_page)
# soup_base = BeautifulSoup(base_page_html.text, 'html.parser')
# product_base = soup_base.find_all('div', {'class': 'StyleT_Item_'})
for page in range(1, 3):
    base_page = "https://www.abc-mart.net/shop/goods/search.aspx?fsgender=2&fscategory=all&p=" + str(page) + "&fscolor=all&fsbrand=SAUCONY&fssize=all#goodslist"
    base_page_html = requests.get(base_page)
    soup_base = BeautifulSoup(base_page_html.text, 'html.parser')
    product_base = soup_base.find_all('div', {'class': 'StyleT_Item_'})
    for product in product_base:
        category_id = 50 #1
        sub_category_id = 61 #2
        category_name = 'shoes' #3
        sub_category_name = 'saucony' #4
        name_vi = product.select_one('a', {'class': 'StyleT_Item_Link_'}).attrs['title'] #5
        name_ja = product.select_one('a', {'class': 'StyleT_Item_Link_'}).attrs['title'] #6
        brand = 'Saucony' #7
        price_div = product.find('div', {'class': 'price_'}).find_all('dd') #8
        unit_price = price_div[0].getText().replace('￥', '').replace(' ', '').replace('(税込)', '').replace(',', '')
        if len(price_div) > 1:
            old_price = price_div[1].getText().replace('￥', '').replace(' ', '').replace('(税込)', '').replace(',', '') #9
        else:
            old_price = None
        # type = 'Giầy New balance nam' #10
        packing = 'Oririn' #11
        use_guide = None #12
        description = None #13
        age_gt = None ## 14
        age_lt = None ## 15
        gender = product.find('div', {'class': 'goods-content_gender'}).getText()
        # print(gender)
        if gender == 'MEN':
            type = 'Giầy Saucony nam' #10
            sex = 'Nam'
        elif gender == 'WOMEN':
            type = 'Giầy Saucony nữ' #10
            sex = 'Nữ'
        else:
            type = 'Giầy Saucony unisex'
            sex = 'Mọi đối tượng'
        # sex = 'male' ## 16
        size = '22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27,27.5,28,28.5,29,30'
        color = None ##17
        image = product.select_one('img').attrs['src'] ##18
        origin_product_code = product.select_one('a', {'class': 'StyleT_Item_Link_'}).attrs['href'].replace('https://www.abc-mart.net/shop/g/', '').replace('/', '') ##19
        origin_url = product.select_one('a', {'class': 'StyleT_Item_Link_'}).attrs['href'] ##20
        active_status = 1 ##21
        stock_status = 1 ##22
        sale_status = 0 ##23
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S") ##24
        data = (category_id, sub_category_id, category_name, sub_category_name, name_vi, name_ja, brand, unit_price, old_price, type, packing, use_guide, description, age_gt, age_lt, sex, size, color, image, origin_product_code, origin_url, active_status, stock_status, sale_status, created)
        print(data)
        if gender == 'WOMEN':
            database.insertProduct(data)
        print("*****************************************************************************************")