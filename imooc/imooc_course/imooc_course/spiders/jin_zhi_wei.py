import time
from urllib.parse import urljoin

import scrapy
from bs4 import BeautifulSoup
from ..items import ImoocCourseItem


class JinZhiWeiSpider(scrapy.Spider):
    name = 'jin_zhi_wei'
    allowed_domains = ['class.imooc.com']
    start_urls = ['https://class.imooc.com/']

    def parse(self, response):
        res = response.text
        soup = BeautifulSoup(res, 'html5lib')
        course_list = soup.find('div', class_='course-row').find_all('div', class_='card')
        item = ImoocCourseItem()
        for course in course_list:
            item['course_name'] = course['data-name']
            item['course_url'] = urljoin(response.url, course['data-url'])
            item['course_cover_img'] = urljoin(response.url, course.find('div', class_='img-con')['style'].replace(
                'background-image:url(', '').replace(')', ''))
            item['course_desc'] = course.find('a', class_='title').string.strip()
            course_price = course.find('div', class_='old-price')
            if course_price:
                item['course_price'] = course_price.string.replace('¥', '').strip()
            else:
                item['course_price'] = ''
            item['course_sale_num'] = course.find('i', class_='imv2-set-sns').find_next('span').string.strip()
            item['course_teacher'] = ''
            item['course_detail_img'] = ''
            item['course_from'] = 1
            item['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            item['deleted_at'] = None
            yield item



