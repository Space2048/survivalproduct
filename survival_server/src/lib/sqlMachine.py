from lib.designpattern import SingletonMeta
from flask_sqlalchemy import SQLAlchemy

class SQLMachine(SingletonMeta):
    def __init__(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Momoca_2019@127.0.0.1:3306/db1"
        self.dbConnect = SQLAlchemy(app)
    @property
    def db():
        return self.dbConnect