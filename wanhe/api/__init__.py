# @Time : 2020/5/20 11:32 下午 
# @Author : CG Zhao
# @File : __init__.py.py 
# @Software: PyCharm
from flask_restful import Api

api = Api()


def init_app(app):
    """
    初始化注册api
    :param app:
    :return:
    """
    api.init_app(app)
