# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookPipeline(object):
    def process_item(self, item, spider):
    	file = open('./data/'+ item['title'],'w')
    	file.write(item['body'].encode('utf-8'))
    	file.close()
        return item
