'''
    博客-配置文件
'''
import os
from app import app
#开发数据库
dev_db = 'sqlite:///'+os.path.join(app.root_path, 'db/data.db')
#系统秘钥(session等使用必须配置)
SECRET_KEY = os.getenv('SECRET_KEY', 'secretkey0001')
#数据库配置
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('SQLITE_DATABASE_URL', dev_db)
#Bootstrap加载本地资源
BOOTSTRAP_SERVE_LOCAL = True