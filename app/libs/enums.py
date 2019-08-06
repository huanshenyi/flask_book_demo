from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # WeChat周り
    USER_MINA = 200
    USER_WX = 201

    # GitHub
    USER_GIT = 300

