from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)
app.config['SECRET_KEY'] = 'insert_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/database'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes

from flask_admin import Admin
from blog.views import AdminView
from blog.models import User, Post, Comment, Checkout, Product
admin = Admin(app, name='Admin panel', template_mode='bootstrap3')
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Comment, db.session))
admin.add_view(AdminView(Product, db.session))
admin.add_view(AdminView(Checkout, db.session))
