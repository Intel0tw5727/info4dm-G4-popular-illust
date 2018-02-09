# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import json


"""画像の基本情報をjsonに書き出すクラス"""
class PixivMetaPipeline(object):

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
        return item

    def open_spider(self, spider):
        settings = spider.settings
        file_path = settings['IMAGES_STORE']+'/meta.json'
        self.file = open(file_path,'w')
        self.file.write('[')
        return

    def close_spider(self,spider):
        self.file.write(']')
        self.file.close()
        return


class PixivImagesPipeline(ImagesPipeline):

    """画像のリンク先を取得する(なければエラーを返す)"""
    def get_media_requests(self, item, info):
        try:
            for image_url in item['img_urls']:
                yield scrapy.Request(image_url,
                headers={'Referer': item['url'],
                         'User-Agent': 'Mozilla/5.0 (Macintosh; '
                                       'Intel Mac OS X 10_10_5) '
                                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                                       'Chrome/45.0.2454.101 Safari/537.36'
                })
        except KeyError:
            raise DropItem("Item contains no images")

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
