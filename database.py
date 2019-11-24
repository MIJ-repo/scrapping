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
        sql = "INSERT INTO `product`(`category_id`, `sub_category_id`, `category_name`, `sub_category_name`, `name_vi`, `name_ja`, `brand`, `unit_price`, `type`, `packing`, `use_guide`, `description`, `age_gt`, `age_lt`, `sex`, `color`, `image`, `origin_product_code`, `origin_url`, `active_status`, `stock_status`, `sale_status`, `created`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.db.execute(sql, data)
            self.connect.commit()
            print('Data saved')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')