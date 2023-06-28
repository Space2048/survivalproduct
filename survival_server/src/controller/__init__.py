'''
controller
@author: blb
@time 23-6-28
'''

from flask import Flask
from controller.pigsty import pigstyBp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint = pigstyBp, url_prefix = "/pigsty" )
    return app