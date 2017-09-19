# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import BiqugeItem, BiqugeContentItem
import scrapy


class BiqugeSpider(Spider):
    name = "biquge"
    allowed_domains = ["konka.com"]

    start_urls = [
        # "http://www.qu.la/",
        # "http://www.qu.la/book/16431/6652064.html",
        "http://www.qu.la/book/16431/6652065.html"
    ]

    # -----instead of start_urls-----
    # def start_requests(self):
    #     return [scrapy.FormRequest("http://eip.konka.com/sys/portal/page.jsp",
    #                                formdata={'j_username': 'zhonghuiming', 'j_password': '0255201314Zhm1'},
    #                                callback=self.logged_in)]


    # def start_requests(self):
    #     yield scrapy.Request('http://www.qu.la/book/16431/6652064.html', self.parse)
    #     yield scrapy.Request('http://www.qu.la/book/16431/6652065.html', self.parse)
    #     yield scrapy.Request('http://www.qu.la/book/16431/6652066.html', self.parse)

    # def logged_in(self,response):
    #     # here you would extract links to follow and return Requests for
    #     # each of them, with another callback
    #     print('login ok!!!!!!!!!!!!!!')
    #     pass
    # -----instead of start_urls-----



    def parse(self, response):
        # self.logger.info('A response from %s just arrived!',response.url)
        print(u'A response from %s just arrived!' % response.url)

        main = BiqugeItem()
        main['title'] = response.xpath('//div[@class="bookname"]/h1/text()').extract()
        main['name'] = response.xpath('//div[@class="con_top"]/a[2]/@title').extract()
        main['link'] = response.url
        yield main


        for txt in response.xpath('//*[@id="content"]/text()').extract():
            item = BiqugeContentItem()
            item['content'] = txt
            yield item

        for url in response.xpath('//*[@id="pager_next"]/@href').extract():
            print('>>>>>>>>>>>>>>>>>> NEXT >>>>>>>>>>>>>>>>>>>')
            print(url)
            yield scrapy.Request("http://www.qu.la/book/16431/" + url, callback=self.parse)



            # src = Selector(response)
            # items = []
            #
            # item = BiqugeItem()
            # item['name'] = src.xpath('//*[@id="wrapper"]/div[6]/div[2]/div[2]/h1/text()').extract()
            # # item['content'] = src.xpath('//*[@id="newscontent"]/div[1]/ul/li[%s]/span[3]/a/text()').extract()
            # item['link'] = src.xpath('//*[@id="pager_next"]/@href').extract()
            # texts = []
            # sites = src.xpath('//*[@id="content"]/text()').extract()
            #
            # for i in range(len(sites)):
            #     text = src.xpath('//*[@id="content"]/text()[%s]' % i).extract()
            #     texts.append(text)
            #
            # item['content'] = texts
            # items.append(item)
            #
            # return items
