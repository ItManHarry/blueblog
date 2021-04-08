'''
    留言板模块
'''
from flask import Blueprint,url_for,redirect,render_template,flash
from blog.forms.board import MessageForm
from blog.models import TbMessage
from app import db
import uuid
#实例化留言板蓝本
bp_board = Blueprint('board', __name__)
#留言板页面
@bp_board.route('/', methods=['GET','POST'])
def index():
    messages = TbMessage.query.order_by(TbMessage.timestamp.desc()).all()
    form = MessageForm()
    if form.validate_on_submit():
        message = TbMessage(id=uuid.uuid4().hex, title=form.title.data, body=form.body.data)
        db.session.add(message)
        db.session.commit()
        flash('消息已发布!!!')
        return redirect(url_for('.index'))   #重定向index视图,获取最新数据,使用蓝本，url_for需要将endpoint添加完整"board.index"，本蓝本内加点即可".index"
    return render_template('board/index.html', form=form, messages=messages)
    #return render_template('board/index.html', form=form)