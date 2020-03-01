import mysql.connector

class Database:

    connect = mysql.connector.connect(
        host='127.0.0.1',
        port='23306',
        db='dev',
        user='root',
        password='nopass',
        # charset='utf8'
    )

    def __init__(self):
        self.db = self.connect.cursor(dictionary=True, buffered=True)


    def insertProduct(self, data):
        # print(data)
        # exit()
        sql = "INSERT INTO `product`(`category_id`, `sub_category_id`, `category_name`, `sub_category_name`, `name_vi`, `name_ja`, `brand`, `unit_price`, `old_price`, `type`, `packing`, `use_guide`, `description`, `age_gt`, `age_lt`, `sex`, `size`, `color`, `image`, `origin_product_code`, `origin_url`, `active_status`, `stock_status`, `sale_status`, `created`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.db.execute(sql, data)
            self.connect.commit()
            print('Data saved')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')

    def selectProductByCategory(self, category_name):
        # print(category_name)
        # exit()
        sql = "SELECT `id`, `origin_url` FROM `product` where `category_name` = %s and id > 34946"
        self.db.execute(sql, (category_name,))
        result = self.db.fetchall()
        return result

    def selectProductBySubCategory(self, sub_category_name):
        # print(category_name)
        # exit()
        sql = "SELECT `id`, `origin_url` FROM `product` where `sub_category_name` = %s"
        self.db.execute(sql, (sub_category_name,))
        result = self.db.fetchall()
        return result

    def updateImage(self, image, id):
        sql = "UPDATE `product` set `description` = %s where `id` = %s"
        try:
            self.db.execute(sql, (image, id))
            self.connect.commit()
            print('Product ID ' + str(id) + ' IMAGE saved')
            print('*************************************************')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')

    def updateStatus(self, id):
        sql = 'UPDATE `product` set `stock_status` = 0, `active_status` = 0 where `id` = %s'
        try:
            self.db.execute(sql, (id,))
            self.connect.commit()
            print('Product ID ' + str(id) + ' stock status saved')
            print('*************************************************')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')

    def selectProductMainImage(self):
        sql = "SELECT `id`, `origin_product_code`, `category_name`, `sub_category_name`, `image` FROM `product` where `category_name` = 'shoes'"
        self.db.execute(sql)
        result = self.db.fetchall()
        return result

    def updateProductMainImage(self, url, id):
        sql = "UPDATE `product` set `image` = %s where `id` = %s"
        try:
            self.db.execute(sql, (url, id))
            self.connect.commit()
            print('Product ID ' + str(id) + ' main image saved')
            print('*************************************************')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')

    def updateSize(self, size, id):
        sql = "UPDATE `product` set `size` = %s where `id` = %s"
        try:
            self.db.execute(sql, (size, id))
            self.connect.commit()
            print('Product '+ str(id) + ' size ' + size + ' updated')
            print('*************************************************')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')