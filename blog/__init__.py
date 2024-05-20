from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)
app.config['SECRET_KEY'] = '76655bf80f7900ae3929c8696951a90c6378b658b9258c2d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dog-ecommerce_owner:o5WMmfxgIsP6@ep-muddy-shadow-a5hlx9b7.us-east-2.aws.neon.tech/dog-ecommerce?options=endpoint%3Dep-muddy-shadow-a5hlx9b7?sslmode=require'

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

if __name__ == '__main__':
  application = app
  application.run(debug=True)





