from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

ENGINE = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/mooc?charset=utf8mb4", echo=False)
Session = sessionmaker(bind=ENGINE)


class MoocCourse(Base):
    __tablename__ = 'mooc_course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_url = Column(String, comment='课程地址')
    course_name = Column(String, index=True, comment='课程名称')
    course_cover_img = Column(String, comment='课程封面图')
    course_desc = Column(String, comment='课程描述')
    course_price = Column(String, comment='课程价格')
    course_teacher = Column(String, index=True, comment='课程讲师')
    course_sale_num = Column(String, comment='课程销量')
    course_detail_img = Column(String, comment='课程详情')
    course_from = Column(String, comment='课程来源')
    created_at = Column(DateTime, comment='创建时间')
    updated_at = Column(DateTime, comment='更新时间')
    deleted_at = Column(DateTime, comment='删除时间')
