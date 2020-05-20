# @Time : 2020/5/20 11:58 下午 
# @Author : CG Zhao
# @File : ext.py 
# @Software: PyCharm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


models = SQLAlchemy()  # 创建一个models对象
migrate = Migrate()


# 导入第三方的库，整合
def init_ext(app):
    models.init_app(app=app)
    migrate.init_app(app, models)  # 初始化迁移配置
    CORS(app)


