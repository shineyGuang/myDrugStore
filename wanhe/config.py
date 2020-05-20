# @Time : 2020/5/20 11:36 下午 
# @Author : CG Zhao
# @File : config.py.py 
# @Software: PyCharm

# 配置基类
class Config:
    """配置文件基类"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session 配置

    # jwt 数字签名
    SIGN = 'xadf@341.A'

    @staticmethod
    def get_db_uri(db_info):
        engine = db_info.get('ENGINE') or 'sqlite'
        driver = db_info.get('DRIVER') or 'sqlite'
        user = db_info.get('USER') or ''
        password = db_info.get('PASSWORD') or ''
        host = db_info.get('HOST') or 'localhost'
        port = db_info.get('PORT') or ''
        name = db_info.get('NAME') or ''
        return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, name)


class DevelopConfig(Config):
    """开发环境配置"""
    DEBUG = True

    # mysql数据库参数
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "ccgg1314papapa",
        "NAME": "wanhe",
        "HOST": "127.0.0.1",  # 到时候换成线上环境数据库
        "PORT": "3306"
    }
    SQLALCHEMY_DATABASE_URI = Config.get_db_uri(db_info)


class TestConfig(Config):
    """测试环境配置类"""
    DEBUG = True
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "ccgg1314papapa",
        "NAME": "wanhe_mirror",
        "HOST": "127.0.0.1",
        "PORT": "3306"
    }
    SQLALCHEMY_DATABASE_URI = Config.get_db_uri(db_info)


class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "ccgg1314papapa",
        "NAME": "wanhe",
        "HOST": "127.0.0.1",  # 到时候换成线上环境数据库
        "PORT": "3306"
    }
    SQLALCHEMY_DATABASE_URI = Config.get_db_uri(db_info)


# 导出对应配置类
envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'product': ProductionConfig
}