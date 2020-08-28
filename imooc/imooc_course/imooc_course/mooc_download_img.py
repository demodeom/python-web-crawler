import os
import time
from urllib.request import urlretrieve

from models.MoocCourse import MoocCourse, Session

session = Session()


def download_img(url, path):
    urlretrieve(url, path)


def get_img_name(url):
    return url.split('/')[-1]


def main():
    for i, in session.query(MoocCourse.course_cover_img):
        img_name = './course_cover_img/' + get_img_name(i)
        if not os.path.exists(img_name):
            download_img(i, img_name)
            time.sleep(1)


if __name__ == '__main__':
    main()
