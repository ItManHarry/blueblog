'''
    留言板-数据存储
'''
from datetime import datetime
from app import db

class TbMessage(db.Model):
    id = db.Column(db.String(40), primary_key=True)
    title = db.Column(db.String(20))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow,index=True)

    def __repr__(self):
        return "<Message body %r>" %self.body

def init_db():
    db.create_all()