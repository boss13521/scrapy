# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class MyspiderPipeline(object):
 #   def process_item(self, item, spider):
 #       return item
class ItcastPipelines(object):
    #init方法是可选的，作为累的初始化方法
    def __init__(self):
        #创建一个文件
        self.filename = open("teacher.json","w")
        #process——item方法必须写的。用来处理item数据
    def process_item(self,item,spider):
        jsontext = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item
        #可选的，结束的时候调用
    def close_spider(self,spider):
        self.filename.close()