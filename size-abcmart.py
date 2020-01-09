# import requests
import requests
from bs4 import BeautifulSoup
from database import Database
database = Database()

category_name = 'shoes'

products = database.selectProductByCategory(category_name)

for product in products:
    product_url = product['origin_url']
    base_page_html = requests.get(product_url)
    soup_base = BeautifulSoup(base_page_html.text, 'html.parser')
    size_div = soup_base.find('div', {'class': 'choosed_size_list'})
    if size_div != None:
        sizes = size_div.select('dl')
        for i in range(len(sizes)):
            if sizes[i].find('div', {'class': 'add-cart-popup'}) != None:
                size_filter = sizes[i].select_one('dt').getText()
                size = size_filter.split('/')
                sizes[i] = size[0].replace(' ', '').replace('cm', '')
            else:
                sizes[i] = None
        available_size = list(filter(None, sizes))
        available_size = ','.join(available_size)

        database.updateSize(available_size, product['id'])
    else:
        database.updateStatus(product['id'])