from flask import Blueprint,render_template,url_for,redirect
bp_admin = Blueprint('admin', __name__)

@bp_admin.route('/')
def index():
    return render_template('index.html')