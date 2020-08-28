# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from .models.MoocCourse import Session, MoocCourse


class ImoocCoursePipeline:

    def __init__(self):
        self.session = Session()

    def process_item(self, item, spider):
        # 数据存储
        """
        以 课程名称 讲师姓名 课程来源 作为课程唯一标识
        如果课程已经存在则跳过
        如果课程不存在则添加
        """
        course = self.session.query(MoocCourse).filter(MoocCourse.course_name == item['course_name']) \
            .filter(MoocCourse.course_teacher == item['course_teacher']) \
            .filter(MoocCourse.course_from == item['course_from']) \
            .first()
        if not course:
            self.session.add(MoocCourse(
                course_url=item['course_url'],
                course_name=item['course_name'],
                course_cover_img=item['course_cover_img'],
                course_desc=item['course_desc'],
                course_price=item['course_price'],
                course_teacher=item['course_teacher'],
                course_sale_num=item['course_sale_num'],
                course_detail_img=item['course_detail_img'],
                course_from=item['course_from'],
                created_at=item['created_at'],
                updated_at=item['updated_at'],
                deleted_at=item['deleted_at']
            ))
            self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()
