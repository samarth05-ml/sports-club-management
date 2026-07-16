from flask import Blueprint

core=Blueprint('core',__name__,url_prefix='/',template_folder='templates')

from . import routes