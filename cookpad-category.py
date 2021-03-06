import requests
import re
import json
from datetime import datetime
from bs4 import BeautifulSoup
from cookpad_db import Database
database = Database()

base_url = 'https://cookpad.com'
root_category_url = 'https://cookpad.com/category/list'
root_category_page_html = requests.get(root_category_url)
soup_root_category_page = BeautifulSoup(root_category_page_html.text, 'html.parser')

root_categories = soup_root_category_page.find_all('li', {'class': 'root_category'})

for root_category in root_categories:
    parent_category_name = root_category.select_one('.root_category_title_wrapper > h2 > a').getText()
    parent_category_origin_url = base_url + root_category.select_one('.root_category_title_wrapper > h2 > a').attrs['href']
    parent_category_data = (1, None, parent_category_name, parent_category_name, parent_category_origin_url, None, None, None, None, 1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    database.insertCategory(parent_category_data)

    parent_category_id = database.selectCategoryByUrl(parent_category_origin_url).get('id')
    # print(parent_category_name + ' has Id: ' + str(parent_category_id))
    child_categories = root_category.select('.sub_category_title')
    for child_category in child_categories:
        child_category_name = child_category.getText().replace('\n', '')
        child_category_origin_url = base_url + child_category.select_one('a').attrs['href']
        child_category_data = (None, parent_category_id, child_category_name, child_category_name, child_category_origin_url, None, None, None, None, 1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        database.insertCategory(child_category_data)

        child_category_id = database.selectCategoryByUrl(child_category_origin_url).get('id')
        child_category_page_html = requests.get(child_category_origin_url)
        soup_child_category_page = BeautifulSoup(child_category_page_html.text, 'html.parser')
        child_lv2_categories = soup_child_category_page.find_all('li', {'class': 'leaf_list'})
        for child_lv2_category in child_lv2_categories:
            if child_lv2_category.select_one('a') != None:
                child_lv2_category_name = child_lv2_category.getText().replace('\n', '')
                child_lv2_category_origin_url = base_url + child_lv2_category.select_one('a').attrs['href']
                child_lv2_category_data = (None, child_category_id, child_lv2_category_name, child_lv2_category_name, child_lv2_category_origin_url, None, None, None, None, 1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print(child_lv2_category_data)
                database.insertCategory(child_lv2_category_data)

                child_lv2_category_id = database.selectCategoryByUrl(child_lv2_category_origin_url).get('id')
                child_lv2_category_page_html = requests.get(child_lv2_category_origin_url)
                soup_child_lv2_category_page = BeautifulSoup(child_lv2_category_page_html.text, 'html.parser')
                child_lv3_categories = soup_child_lv2_category_page.find_all('li', {'class': 'leaf_list'})
                for child_lv3_category in child_lv3_categories:
                    if child_lv3_category.select_one('a') != None:
                        child_lv3_category_name = child_lv3_category.getText().replace('\n', '')
                        child_lv3_category_origin_url = base_url + child_lv3_category.select_one('a').attrs['href']
                        child_lv3_category_data = (None, child_lv2_category_id, child_lv3_category_name, child_lv3_category_name, child_lv3_category_origin_url, None, None, None, None, 1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        print(child_lv3_category_data)
                        database.insertCategory(child_lv3_category_data)


