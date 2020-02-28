import mysql.connector

class Database:

    connect = mysql.connector.connect(
        host='127.0.0.1',
        port='23306',
        db='line-api',
        user='root',
        password='nopass',
        # charset='utf8'
    )

    def __init__(self):
        self.db = self.connect.cursor(dictionary=True, buffered=True)

    def selectChildCategory(self):
        sql = "SELECT `id`, `origin_url` FROM `category` where `parent_flag` IS NULL"
        self.db.execute(sql)
        result = self.db.fetchall()
        return result

    def selectCategoryByUrl(self, origin_url):
        sql = "SELECT `id` FROM `category` where `origin_url` = %s"
        self.db.execute(sql, (origin_url,))
        result = self.db.fetchall()
        return result[0]

    def getParentsCategory(self):
        sql = "SELECT `id` FROM `category` where `parent_flag` = 1"
        self.db.execute(sql)
        result = self.db.fetchall()
        return result

    def getChildrenCategoryByParentId(self, parents_id):
        sql = "SELECT `id`, `origin_url` from `category` where `group_id` = %s"
        self.db.execute(sql, (parents_id,))
        result = self.db.fetchall()
        return result

    def getChildrenCategoryByParentIdExcept(self, parents_id):
        sql = "SELECT `id`, `origin_url` from `category` where `group_id` = %s and id > 55"
        self.db.execute(sql, (parents_id,))
        result = self.db.fetchall()
        return result

    def insertCategory(self, data):
        
        sql = "INSERT INTO `category` (`parent_flag`, `group_id`, `name_en`, `name_jp`, `origin_url`, `image`, `meta_title`, `meta_description`, `meta_keywords`, `active_status`, `created`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.db.execute(sql, data)
            self.connect.commit()
            print('Category saved')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')

    def insertProductOriginUrl(self, data):
        sql = "INSERT INTO `product` (`category_id`, `code`, `origin_url`, `created`) VALUES (%s, %s, %s, %s)"
        try:
            self.db.execute(sql, data)
            self.connect.commit()
            print('Product URL saved')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print(error)
            print('-------------------------------------------------')