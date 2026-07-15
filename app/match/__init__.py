from flask import Blueprint

match=Blueprint('match',__name__,url_prefix='/match',template_folder='templates')

from . import routes