import time
from urllib.parse import urljoin

import scrapy
from bs4 import BeautifulSoup
from ..items import ImoocCourseItem


class ShiZhanSpider(scrapy.Spider):
    name = 'shi_zhan'
    allowed_domains = ['coding.imooc.com']
    start_urls = ['https://coding.imooc.com/']

    def parse(self, response):
        # print(dir(response))
        res = response.text
        item = ImoocCourseItem()
        soup = BeautifulSoup(res, 'html5lib')

        # 课程信息
        course_list = soup.find_all('div', class_='shizhan-course-wrap')

        for course in course_list:
            item['course_url'] = urljoin(response.url, course.find('a')['href'])
            item['course_cover_img'] = urljoin(response.url, course.find('img', class_='shizhan-course-img')['src'])
            item['course_name'] = course.find('p', class_='shizan-name').string.strip()
            item['course_desc'] = course.find('p', class_='shizan-desc').string.strip()

            course_price = course.find('div', class_='course-card-price')
            if not course_price:
                course_price = course.find('span', class_='cost-price')
            item['course_price'] = course_price.string.replace('￥', '').strip()

            item['course_sale_num'] = course.find('i', class_='imv2-set-sns').next_element.string
            item['course_detail_img'] = ''
            item['course_from'] = 1
            item['course_teacher'] = course.find('div', class_='lecturer-info').find('span').string.strip()

            item['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            item['deleted_at'] = None
            # print('-'.center(20, '-'))
            # print(item)
            yield item

        # 下一页
        next_page_soup = soup.find('a', text='下一页')
        if next_page_soup:
            next_page_url = urljoin(response.url, next_page_soup['href'])
            # print(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
