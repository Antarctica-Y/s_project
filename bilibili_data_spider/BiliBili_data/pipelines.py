# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class BilibiliDataPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(host='localhost',
                     user='root',
                     password='RDeFKxhBFzHmcFGH',
                     port = 3306,
                     database='bili_data'
                                  )
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        info = dict(item)
        for key,value in info.items():
            if key != 'id':
                if type(value) == str:
                    sql = 'insert into bili_data(id, %s) values (%d, "%s") on duplicate key update %s = "%s";' % (key, info['id'], value, key, value)
                elif type(value) == int:
                    sql = 'insert into bili_data(id, %s) values (%d, %d) on duplicate key update %s = %d;' % (key, info['id'], value, key, value)
                try:
                    # 执行sql语句
                    self.cursor.execute(sql)
                    # 执行sql语句
                    self.db.commit()
                except:
                    print("Error")
                    with open('./logs.txt', 'a') as f:
                        f.write(sql + '\n')
                        f.write(key + '写入错误' + '\n')
                        # 发生错误时回滚
                    self.db.rollback()
        return item
