# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import time
import string
import urllib
import os.path


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class BiqugePipeline(object):
    def __init__(self):
        print('############### INIT BiqugePipeline  ##############')

    def open_spider(self, spider):
        print('############### open_spider   ##############')
        # self.file = open('items.json', 'wb')
        # self.file = codecs.open('items.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print('############### close_spider   ##############')
        # self.file.close()

    def process_item(self, item, spider):
        # print '############### process_item ##############'
        # print item["content"]

        print('############### process_item ##############')
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line.decode('unicode_escape'))


        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.txt'
        with open(fileName, 'a') as fp:
            # for i in item['name']:
            #     fp.write(i.encode('utf-8'))
            # fp.write('\t')

            # print(len(item['content']))

            for i in item['content']:
                fp.write(i)
                print(i)
            fp.write('\t')

            # for i in item['link']:
            #     fp.write(i.encode('utf-8'))
            # fp.write('\t')

            # fp.write(item['name'] + '\t')
            # fp.write(item['content']+ '\t')
            # fp.write(item['link'] + '\n\n')
            # time.sleep(1)

        return item
