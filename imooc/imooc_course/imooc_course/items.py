# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImoocCourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    course_url = scrapy.Field()
    course_name = scrapy.Field()
    course_cover_img = scrapy.Field()
    course_desc = scrapy.Field()
    course_price = scrapy.Field()
    course_teacher = scrapy.Field()
    course_sale_num = scrapy.Field()
    course_detail_img = scrapy.Field()
    course_from = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    deleted_at = scrapy.Field()
