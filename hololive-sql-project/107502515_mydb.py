import pymysql
#創建資料庫類
class Sql_operation(object):
    #資料庫連接
    def __init__(self, mydb):
        #傳入資料庫名稱
        self.mydb = mydb
        #打開資料庫連接
        self.db = pymysql.connect(
            host="localhost", user="root", password="aelth97", db=self.mydb, charset="utf8")
        #創建暫存cache
        self.cursor = self.db.cursor()
    #查看TABLE的func
    def FindAll(self, table_name):
        #傳入table名稱
        self.table_name = table_name
        #SQL語法
        sql = "select * from %s" % (self.table_name)
        try:
            #執行資料庫
            self.cursor.execute(sql)
            #取得所有結果列
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print("SQL執行失敗，原因：", err)
    #新增資料func
    def Insert(self, holo_name, holo_gender, holo_age, holo_height, holo_alias, holo_group):
        #傳入引數
        self.holo_name = holo_name
        self.holo_gender = holo_gender
        self.holo_age = holo_age
        self.holo_height = holo_height
        self.holo_alias = holo_alias
        self.holo_group = holo_group
        #SQL語法
        sql = "insert into holo_info(holo_name,holo_gender,holo_age,holo_height,holo_alias,holo_group) values('%s','%s','%s','%s','%s','%s')" % (
            self.holo_name, self.holo_gender, self.holo_age, self.holo_height, self.holo_alias, self.holo_group)
        try:
            #執行資料庫
            self.cursor.execute(sql)
            #提交
            self.db.commit()
        except Exception as err:
            #轉返
            self.db.rollback()
            print("SQL執行失敗，原因：", err)   
    #刪除資料func
    def Del(self, holo_id):
        #傳入holo_id
        self.holo_id = holo_id
        #SQL語法
        sql = "delete from holo_info where id=%d" % (self.holo_id)
        try:
            #執行資料庫
            self.cursor.execute(sql)
            #提交
            self.db.commit()
        except Exception as err:
            #轉返
            self.db.rollback()
            print("SQL執行失敗，原因：", err)
    #用func關閉資料庫
    def __del__(self):
        #關閉資料庫連接
        self.db.close()