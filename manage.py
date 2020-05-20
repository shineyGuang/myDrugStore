# @Time : 2020/5/20 11:32 下午 
# @Author : CG Zhao
# @File : manage.py.py 
# @Software: PyCharm


from flask_migrate import MigrateCommand
from wanhe import create_app
from flask_script import Manager


app = create_app()  # 注册了app和返指定的配置，返回app
manager = Manager(app)  # 将app注册到脚本管理器中

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    # app.run(host="127.0.0.1", port=5000)
