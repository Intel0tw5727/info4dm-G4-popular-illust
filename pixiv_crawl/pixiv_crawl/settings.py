# -*- coding: utf-8 -*-

# Scrapy settings for pixiv_crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import datetime
import os

BOT_NAME = 'pixiv_crawl'

SPIDER_MODULES = ['pixiv_crawl.spiders']
NEWSPIDER_MODULE = 'pixiv_crawl.spiders'

ITEM_PIPELINES = {
    'pixiv_crawl.pipelines.PixivImagesPipeline': 1,
    'pixiv_crawl.pipelines.PixivMetaPipeline': 10
  }

LOG_LEVEL = "INFO"

# json 出力の文字コード
FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOAD_DELAY = 1
COOKIES_ENABLED = True
# COOKIES_DEBUG = True
IMAGES_STORE = './download_image_'	#画像の保存先

#########USER INFO
PIXIV_USER_NAME = os.getenv("PIXIV_USER_NAME")
PIXIV_USER_PASS = os.getenv("PIXIV_USER_PASS")
#########HOST INFO
START_DATE = datetime.date(2017,10,24)    #検索日時
#########PXIIV_MODE
__PIXIV_MODES__ = [
    'daily',        #0 デイリーランキング
    'weekly',       #1 ウィークリーランキング
    'monthly',      #2 マンスリーランキング
    'male',         #3 男性向けイラストランキング
    'female',       #4 女性向けイラストランキング
    'daily_r18',    #5 18歳以上向けデイリー
    'weekly_r18',   #6 18歳以上向けウィークリー
    'male_r18',     #7 18歳以上男性向け
    'female_r18'    #8 18歳以上女性向け
]
__SELECT_MODE_IDX__ = 2 #__PIXIV_MODES__のMODE選択
SELECT_MODE = __PIXIV_MODES__[__SELECT_MODE_IDX__]  #IMAGES_STOREにmodeを渡す
########GENERATE IMAGE STORE
IMAGES_STORE = IMAGES_STORE + '{mode}/{year}{month}{day}'.format(
                        year=START_DATE.year,
                        month=str(START_DATE.month).zfill(2),
                        day=str(START_DATE.day).zfill(2),
                        mode = SELECT_MODE
                )

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pixiv_crawl (+http://www.yourdomain.com)'
