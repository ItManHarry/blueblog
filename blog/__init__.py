from blog.views.auth import bp_auth
from blog.views.admin import bp_admin
from blog.views.blog import bp_blog
from blog.views.board import bp_board
#蓝本注册
def register_blueprints(app):
    #注册蓝本
    app.register_blueprint(bp_auth,  url_prefix='/auth')
    app.register_blueprint(bp_admin, url_prefix='/admin')
    app.register_blueprint(bp_blog,  url_prefix='/blog')
    app.register_blueprint(bp_board, url_prefix='/board')