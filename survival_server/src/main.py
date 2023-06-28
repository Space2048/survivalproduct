from flask import Flask
from controller import create_app
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

app = create_app()
#app.config["SECRET_KEY"] = "Momoca_2019"
app.config["SQLALCHEMY_DATABASE_URI"] = "xxxxx"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

# 创建模型类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
 
    def __init__(self, username, email):
        self.username = username
        self.email = email
 
    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == "__main__":
    
    db.create_all()
    admin = User('admin', 'admin@example.com')
    guest = User('guest', 'guest@example.com')
    # 写入到数据库
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    # 访问数据库
    users = User.query.all()
    admin = User.query.filter_by(username='admin').first()
    print(users)
    print(admin)

    #app.run(host="0.0.0.0", port=5423, debug=True)
    