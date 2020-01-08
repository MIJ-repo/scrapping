# import urllib
from urllib import request
import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from database import Database
database = Database()

# f = open('00000002.jpg', 'wb')
# f.write(request.urlopen("https://www.matsukiyo.co.jp/store/image/4987084410979_t1").read())
# f.close()
# request.urlretrieve('https://www.matsukiyo.co.jp/store/image/4987084410979_t1', '/home/long/Desktop/4987084410979_t1')
# exit()
products = database.selectProductByCategory('shoes')
# main_path = '/home/long/Desktop/product_img/'
# main_url = 'https://mij.vn/laravel-filemanager/images/shares/product/'
for product in products:
    print(product)
    exit()
    # if not os.path.exists(main_path + product['category_name']):
    #     os.makedirs(main_path + product['category_name'])
    #     print(main_path + product['category_name'] + ' created')
    # if not os.path.exists(main_path + product['category_name'] + '/' + product['sub_category_name']):
    #     os.makedirs(main_path + product['category_name'] + '/' + product['sub_category_name'])
    #     print(main_path + product['category_name'] + '/' + product['sub_category_name'] + ' created')
    # img_name = product['origin_product_code'] + '.jpg'
    # save_path = main_path + product['category_name'] + '/' + product['sub_category_name'] + '/' + img_name
    # request.urlretrieve(product['image'], save_path)
    # print('product' + str(product['id']) + ' image saved to local')
    # print('--------------------------------------------------------------------')
    # product_url = str(main_url + product['category_name'] + '/' + product['sub_category_name'] + '/' + product['origin_product_code'] + '.jpg')
    # database.updateProductMainImage(product_url, product['id'])
    # print(product_url)
    # exit()