from flask import Blueprint

team=Blueprint('team',__name__,url_prefix='/team',template_folder='templates')

from . import routes