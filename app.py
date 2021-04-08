from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap
#执行Flask实例创建
app = Flask('blog')
app.debug = True
#导入配置
app.config.from_pyfile('settings.py')
#创建Bootstrap实例
boostrap = Bootstrap(app)
#创建时间控件Moment实例
moment = Moment(app)
#删除Jinja2 语句后的第一个空行
app.jinja_env.trim_blocks=True
#删除Jinja2 语句所在行之前的空格和制表符(tabs)
app.jinja_env.lstrip_blocks=True
#数据库实例
db = SQLAlchemy(app)
#初始化数据库
from blog.models import init_db
init_db()
#注册蓝本
'''
    采坑记录：
    背景：加载蓝本，开始放在了最顶端，然后系统报错如下：
    ImportError: cannot import name 'db' from partially initialized module 'app' (most likely due to a circular import) 
    (D:\Development\Python\projects\blueblog\app.py)
    原因：导入board模块的时候，db并未实例化，故报错
    解决：将蓝本注册写到最下面，保证所有的对象均已实例化，问题解决！！！
'''
from blog import register_blueprints
register_blueprints(app)
#错误页面跳转
from blog import errors