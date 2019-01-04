# -*- coding: utf-8 -*-
import json
import pymongo
from scrapy.conf import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        #self.filename = open("douban250.json","w")




        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        #创建mongodb数据库链接
        client = pymongo.MongoClient(host,port)

        #指定数据库
        mydb = client[dbname]

        #存放数据的数据库表名
        self.mysheet = mydb[sheetname]



    def process_item(self, item, spider):
        data = dict(item)
        self.mysheet.insert(data)

        #text = json.dumps(dict(item),ensure_ascii=False) +"\n"

        #self.filename.write(text.encode("utf-8"))


        return item


    #def close_spider(self):
      #  self.filename.close()