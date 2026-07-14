from flask import Blueprint

training=Blueprint('training',__name__,url_prefix='/training')

from . import routes