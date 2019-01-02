#coding=utf-8

import scrapy
from mySpider.items import MyspiderItem

class ItcastSpdier(scrapy.Spider):
    #爬虫名
    name = "itcast"
    #允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    #爬虫起始的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

    def parse(self, response):

        #
        #保存到本地
        #with open("teacher.html","w") as f:
        #f.write(response.body)
        teacher_list = response.xpath('//div[@class="li_txt"]')
        #print teacher_list
        #teacheritem = []
        for each in teacher_list:
            item = MyspiderItem()
            #extract()将匹配出来的结果转换为unicode字符串
            name = each.xpath('./h3/text()').extract()
            #title
            title = each.xpath('./h4/text()').extract()
            #info
            info = each.xpath('./p/text()').extract()

            #item["name"] = name[0].encode("gbk")
            #item['title'] = title[0].encode("gbk")
            #'gbk' codec can't encode character u'\xa0' in position 95: illegal multibyte sequence
            # item['info'] = info[0].encode("gbk")
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            #teacheritem.append(item)
            #print teacheritem
        #return teacheritem


            yield item