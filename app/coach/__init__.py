from flask import Blueprint

coach=Blueprint('coach',__name__,url_prefix='/coach')

from . import routes