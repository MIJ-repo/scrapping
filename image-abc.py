# import requests
import requests
from bs4 import BeautifulSoup
from database import Database
database = Database()

category_name = 'shoes'

products = database.selectProductByCategory(category_name)
for product in products:
    # print(product)
    # exit()
    product_url = product['origin_url']
    base_page_html = requests.get(product_url)
    soup_base = BeautifulSoup(base_page_html.text, 'html.parser')
    image_div = soup_base.find('div', {'class': 'goodsimg'})
    if image_div != None:
        images = image_div.select('.img_container > img')
        # print(images)
        # exit()
        for i in range(len(images)):
            if images[i].has_attr('data-zoom-image'):
                images[i] = '<img src="' + images[i].attrs['data-zoom-image'] + '">'
            else:
                images[i] = '<img src="' + images[i].attrs['src'] + '">'
        images = '</br></br>'.join(images) ## 15
        # print(images)
        # exit()
        database.updateImage(images, product['id'])
        # print(images)
        # exit()