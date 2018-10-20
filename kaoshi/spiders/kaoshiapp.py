# -*- coding: utf-8 -*-
import scrapy
from kaoshi.items import KaoshiItem

class KaoshiappSpider(scrapy.Spider):
    name = 'kaoshiapp'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-0']

    def parse(self, response):
        #所有链接信息
        div_list=response.xpath('//div[@class="channel-con"]/ul[@class="video-list"]/li')
        for odiv in div_list:

            item = KaoshiItem()
            item['imgage_url']=odiv.xpath('.//a/img/@_src')[0].extract().strip('\n\r\t')
            item['imgage_name']=odiv.xpath('.//div[@class="video-con-top"]/a/p/text()')[0].extract().strip('\n\r\t')
            item['video_author']=odiv.xpath('.//div/div[2]/a/span[2]/text()')[0].extract().strip('\n\r\t')
            item['video_date']=odiv.xpath('.//a/div[2]/p/text()')[0].extract().strip('\n\r\t发布')
            yield item





