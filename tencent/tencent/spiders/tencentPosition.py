# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = "tencentPosition"
    allowed_domains = ["tencent.com"]
    url = "https://hr.tencent.com/position.php?start="
    offset = 0
    start_urls = [
        url + str(offset),
    ]

    def parse(self, response):
        #pass
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            #初始化模型对象
            item = TencentItem()
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()
            # 招聘人数
            item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item


        if self.offset < 2830:
            self.offset += 10
        else:
            # break
            raise "结束工作"
        # 这里的self。parse后面没有（）。

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)