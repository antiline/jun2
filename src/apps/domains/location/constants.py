from libs.base.constants import BaseConstant


class GpxPointRefType(BaseConstant):
    GPX = 0
    EXIF = 1
    USER = 2

    _LIST = [GPX, EXIF, USER, ]
    _STRING_MAP = {
        GPX: 'GPX crawl',
        EXIF: 'Extract from exif',
        USER: 'by User',
    }
