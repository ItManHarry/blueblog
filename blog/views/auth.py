from flask import Blueprint,render_template,session
bp_auth = Blueprint('auth', __name__)

#登录
@bp_auth.route('/login')
def login():
    return render_template('auth/login.html')
#登出
@bp_auth.route('/logout')
def logout():
    return render_template('auth/logout.html')