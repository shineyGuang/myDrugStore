# @Time : 2020/5/20 11:31 下午 
# @Author : CG Zhao
# @File : __init__.py.py 
# @Software: PyCharm
from flask import Flask

from wanhe.config import envs
from wanhe.ext import init_ext
from wanhe.api import init_app


def create_app():
    """
    初始化app，完成相应配置
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(envs.get('develop') or 'develop')
    init_ext(app)  # 初始化第三方库
    init_app(app)  # 注册api
    return app


